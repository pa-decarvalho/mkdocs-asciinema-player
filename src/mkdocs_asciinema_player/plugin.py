"""
MkDocs Asciinema Player Plugin.

This module defines the AsciinemaPlayerPlugin for embedding Asciinema player in MkDocs.

Author: De Carvalho Philippe-Andre
"""
import os
import re
import shutil
import logging
import json
from json import JSONDecodeError
from typing import cast, Any, Optional, Match, Dict
from urllib.parse import urlparse
from jinja2 import Environment, PackageLoader
from mkdocs.__main__ import ColorFormatter
from mkdocs.plugins import BasePlugin
from mkdocs.config.base import Config
from mkdocs.config.config_options import Type
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files, File


class AsciinemaPlayerConfig(Config):
    """
    Configuration class for the AsciinemaPlayerPlugin.
    """
    loglevel = Type(str, default="INFO")


class AsciinemaPlayerPlugin(BasePlugin[AsciinemaPlayerConfig]):
    """
    Plugin for embedding Asciinema player in MkDocs.

    Methods:
        parse_json: Parses JSON content and returns the resulting object.
        render_template: Renders a Jinja2 template with the given data.
        validate_config: Validates the user configuration for the AsciinemaPlayerPlugin.
        replace_asciinema_player_match: Replaces the matched Asciinema player block with the rendered template.
        on_page_markdown: Callback function called when processing page markdown.
        on_files: Callback function called when copying additional files during the MkDocs build process.
        on_config: Callback function called to modify the MkDocs configuration.
    """
    default_configs = {
        "parameters": [
            {"name": "file", "default": ""},
            {"name": "title", "default": "Terminal"},
            {"name": "mkap_theme", "default": "night"},
            {"name": "cols", "default": 80},
            {"name": "rows", "default": 24},
            {"name": "auto_play", "default": False},
            {"name": "preload", "default": False},
            {"name": "loop", "default": False},
            {"name": "start_at", "default": "0:00"},
            {"name": "speed", "default": 1.0},
            {"name": "theme", "default": "asciinema"},
            {"name": "fit", "default": "width"},
            {"name": "controls", "default": "auto"},
            {"name": "pause_on_markers", "default": False},
            {"name": "terminal_font_size", "default": "small"},
            {"name": "terminal_line_height", "default": "1.33333333"},
        ]
    }
    loglevel_config = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "FATAL": logging.FATAL,
    }

    def __init__(self) -> None:
        """
        Initializes an instance of the AsciinemaPlayerPlugin.
        """
        self.mkdocs_config = MkDocsConfig()
        self.site_url = ""
        self.match_id = 0

    def init_logging(self) -> None:
        self.log = logging.getLogger(__name__)
        self.log.setLevel(self.loglevel_config.get(self.config.loglevel, logging.INFO))
        self.log.propagate = False
        stream = logging.StreamHandler()
        stream.setFormatter(ColorFormatter())
        stream.name = "MkDocsStreamHandler"
        self.log.addHandler(stream)

    def parse_json(self, content: str) -> Any:
        """
        Parses JSON content and returns the resulting object.

        Args:
            content (str): The JSON content to be parsed.

        Returns:
            Any: The parsed JSON object, or None if an error occurs during parsing.
        """
        try:
            return json.loads(content)
        except JSONDecodeError as e:
            self.log.error(f"[mkdocs-asciinema-player][{self.match_id}] JSONDecodeError: {e}")
        return None

    def render_template(self, data: dict[Any, Any]) -> str:
        """
        Renders a Jinja2 template with the given data.

        Args:
            data (dict): The data to be passed to the Jinja2 template.

        Returns:
            str: The rendered template as a string.
        """
        self.log.info(f"[mkdocs-asciinema-player][{self.match_id}] Rendering template")
        env = Environment(
            loader=PackageLoader("mkdocs_asciinema_player", "templates"),
            lstrip_blocks=True,
            trim_blocks=True,
            autoescape=True,
        )
        return env.get_template("asciinema-player.html").render(data)

    def validate_config(self, user_config: dict[str, Any]) -> bool:
        """
        Validates the user configuration for the AsciinemaPlayerPlugin.

        Args:
            user_config (dict): The user-provided configuration for the plugin.

        Returns:
            bool: True if the configuration is valid, False otherwise.
        """
        self.log.info(f"[mkdocs-asciinema-player][{self.match_id}] Validating user config: {user_config}")
        parameters = self.default_configs.get("parameters", [])
        if "file" not in user_config:
            self.log.error(f"[mkdocs-asciinema-player][{self.match_id}] Property 'file' not found inside user config")
            return False
        themes_dir = os.path.join(os.path.dirname(__file__), "templates", "themes")
        available_themes = [
            os.path.splitext(f)[0] 
            for f in os.listdir(themes_dir) 
            if f.endswith('.html')
        ]

        for param in parameters:
            param = cast(Dict[str, Any], param)
            param_name = param["name"]
            param_type = type(param["default"])

            if param_name in user_config:
                user_value = user_config[param_name]
                if param_name == 'mkap_theme':
                    if user_value not in available_themes:
                        self.log.error(f"[mkdocs-asciinema-player][{self.match_id}] Invalid theme '{user_value}': Available themes are {available_themes}")
                        return False
                elif not isinstance(user_value, param_type):
                    self.log.error(f"[mkdocs-asciinema-player][{self.match_id}] Parameter '{param_name}' should be of type {param_type} but got {type(user_value).__name__}")
                    return False
            elif "default" in param:
                default_param = param["default"] # declaring 'default_param' variable to be able to print it (can't use 'param["default"]' in a f-string in python bellow 3.12)
                self.log.debug(f"[mkdocs-asciinema-player][{self.match_id}] Setting default value '{default_param}' for parameter '{param_name}'")
                user_config[param_name] = default_param

        return True

    def replace_asciinema_player_match(self, match: Match[str]) -> str:
        """
        Replaces the matched Asciinema player block with the rendered template.

        Args:
            match (re.Match): The regular expression match object.

        Returns:
            str: The replacement string.
        """
        self.log.info(f"[mkdocs-asciinema-player][{self.match_id}] Replacing asciinema-player block for match {self.match_id}")
        parsed_json = self.parse_json(match.group(1))
        if not self.validate_config(parsed_json) or parsed_json is None:
            self.log.info(f"[mkdocs-asciinema-player][{self.match_id}] Skipping replace")
            return ""
        parsed_json["file_path"] = self.site_url + parsed_json["file"]
        parsed_json["match_id"] = self.match_id
        template = self.render_template(parsed_json)
        self.match_id += 1
        return template

    # pylint: disable-next=unused-argument
    def on_page_markdown(self, markdown: str, page: Page, config: MkDocsConfig, files: Files) -> Optional[str]:
        """
        Callback function called when processing page markdown.

        This function searches for Asciinema player blocks in the markdown content and replaces them with
        the rendered template containing the specified Asciinema player configuration.

        Args:
            markdown (str): The markdown content of the page.
            page (Page): The current page being processed.
            config (MkDocsConfig): The MkDocs configuration object.
            files (Files): The file structure of the MkDocs project.

        Returns:
            Optional[str]: The modified markdown content or None if no modification is needed.
        """
        return re.sub(
            re.compile(r"```asciinema-player\n(.*?)\n```", re.DOTALL),
            self.replace_asciinema_player_match,
            markdown
        )

    def on_files(self, files: Files, config: Config) -> Files:
        """
        Callback function called when copying additional files during the MkDocs build process.

        This function is responsible for copying necessary files, such as CSS and JavaScript files,
        required for embedding the Asciinema player in the MkDocs documentation.

        Args:
            files (Files): The file structure of the MkDocs project.
            config (MkDocsConfig): The MkDocs configuration object.

        Returns:
            Files: The modified file structure after copying additional files.
        """
        self.log.info("[mkdocs-asciinema-player] Adding assets files to the build")
        assets_src_dir = os.path.join(os.path.dirname(__file__), "assets")
        css_dest_dir = os.path.join(config["site_dir"], "css")
        js_dest_dir = os.path.join(config["site_dir"], "js")
        icons_dest_dir = os.path.join(css_dest_dir, "icons")

        terminal_player_css_file_obj = File(
            path="terminal-player.css",
            src_dir=assets_src_dir,
            dest_dir=css_dest_dir,
            use_directory_urls=config["use_directory_urls"],
        )
        asciinema_css_file_obj = File(
            path="asciinema-player.css",
            src_dir=assets_src_dir,
            dest_dir=css_dest_dir,
            use_directory_urls=config["use_directory_urls"],
        )
        asciinema_js_file_obj = File(
            path="asciinema-player.min.js",
            src_dir=assets_src_dir,
            dest_dir=js_dest_dir,
            use_directory_urls=config["use_directory_urls"],
        )

        files.append(terminal_player_css_file_obj)
        files.append(asciinema_css_file_obj)
        files.append(asciinema_js_file_obj)
        shutil.copytree(assets_src_dir + "/icons", icons_dest_dir)

        return files

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig:
        """
        Callback function called to modify the MkDocs configuration.

        This function updates the MkDocs configuration to include the paths
        of the copied CSS and JavaScript files required for Asciinema player.

        Args:
            config (MkDocsConfig): The MkDocs configuration object.

        Returns:
            MkDocsConfig: The modified MkDocs configuration.
        """
        self.mkdocs_config = config
        self.init_logging()
        self.site_url = urlparse(self.mkdocs_config["site_url"]).path or ""
        self.log.info("[mkdocs-asciinema-player] Adding extra_css and extra_javascript to the config")
        config["extra_css"].append("css/terminal-player.css")
        config["extra_css"].append("css/asciinema-player.css")
        config["extra_javascript"].append("js/asciinema-player.min.js")
        return config
