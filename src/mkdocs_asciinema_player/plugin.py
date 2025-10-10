"""
MkDocs Asciinema Player Plugin.

This module defines the AsciinemaPlayerPlugin for embedding Asciinema player in MkDocs.

Author: De Carvalho Philippe-Andre
"""

import json
import logging
import re
import shutil
from json import JSONDecodeError
from pathlib import Path
from re import Match
from typing import Any, cast
from urllib.parse import urlparse

from jinja2 import Environment, PackageLoader
from mkdocs.__main__ import ColorFormatter
from mkdocs.config.base import Config
from mkdocs.config.config_options import Type
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page


class AsciinemaPlayerConfig(Config):
    """Configuration class for the AsciinemaPlayerPlugin."""

    plugin_name = "[mkdocs-asciinema-player]"
    loglevel = Type(str, default="INFO")


class AsciinemaPlayerPlugin(BasePlugin[AsciinemaPlayerConfig]):
    """Plugin for embedding Asciinema player in MkDocs."""

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
        ],
    }
    loglevel_config = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "FATAL": logging.FATAL,
    }

    def __init__(self) -> None:
        """Init the AsciinemaPlayerPlugin class."""
        self.mkdocs_config = MkDocsConfig()
        self.site_url = ""
        self.match_id = 0

    def init_logging(self) -> None:
        """Init the logging module."""
        self.log = logging.getLogger(__name__)
        self.log.setLevel(self.loglevel_config.get(self.config.loglevel, logging.INFO))
        self.log.propagate = False
        stream = logging.StreamHandler()
        stream.setFormatter(ColorFormatter())
        stream.name = "MkDocsStreamHandler"
        self.log.addHandler(stream)

    def parse_json(self, content: str) -> Any:
        """
        Return an object with the given JSON content.

        Args:
            content (str): The JSON content to be parsed.

        Returns:
            Any: The parsed JSON object, or None if an error occurs during parsing.

        """
        try:
            return json.loads(content)
        except JSONDecodeError:
            self.log.exception(
                "%s[%s] JSONDecodeError",
                self.config.plugin_name,
                self.match_id,
            )
            return None
        return None

    def render_template(self, data: dict[Any, Any]) -> str:
        """
        Return a rendered Jinja2 template with the given data.

        Args:
            data (dict): The data to be passed to the Jinja2 template.

        Returns:
            str: The rendered template as a string.

        """
        self.log.info(
            "%s[%s] Rendering template",
            self.config.plugin_name,
            self.match_id,
        )
        env = Environment(
            loader=PackageLoader("mkdocs_asciinema_player", "templates"),
            lstrip_blocks=True,
            trim_blocks=True,
            autoescape=True,
        )
        return env.get_template("asciinema-player.html").render(data)

    def validate_config(self, user_config: dict[str, Any]) -> bool:
        """
        Return True if the configuration is valid, False otherwise.

        Args:
            user_config (dict): The user-provided configuration for the plugin.

        Returns:
            bool: True if the configuration is valid, False otherwise.

        """
        self.log.info(
            "%s[%s] Validating user config: %s",
            self.config.plugin_name,
            self.match_id,
            user_config,
        )
        parameters = self.default_configs.get("parameters", [])
        if "file" not in user_config:
            self.log.error(
                "%s[%s] Property 'file' not found inside user config",
                self.config.plugin_name,
                self.match_id,
            )
            return False
        themes_dir = Path(__file__).parent / "templates" / "themes"
        available_themes = [p.stem for p in themes_dir.glob("*.html")]

        for param in parameters:
            param = cast("dict[str, Any]", param)
            param_name = param["name"]
            param_type = type(param["default"])

            if param_name in user_config:
                user_value = user_config[param_name]
                if param_name == "mkap_theme":
                    if user_value not in available_themes:
                        self.log.error(
                            "%s[%s] Invalid theme '%s': Available themes are %s",
                            self.config.plugin_name,
                            self.match_id,
                            user_value,
                            available_themes,
                        )
                        return False
                elif not isinstance(user_value, param_type):
                    self.log.error(
                        "%s[%s] Parameter '%s' should be of type %s but got %s",
                        self.config.plugin_name,
                        self.match_id,
                        param_name,
                        param_type,
                        type(user_value).__name__,
                    )
                    return False
            elif "default" in param:
                self.log.debug(
                    "%s[%s] Setting default value '%s' for parameter '%s'",
                    self.config.plugin_name,
                    self.match_id,
                    param["default"],
                    param_name,
                )
                user_config[param_name] = param["default"]

        return True

    def replace_asciinema_player_match(self, match: Match[str]) -> str:
        """
        Return the matched Asciinema player block with the rendered template.

        Args:
            match (re.Match): The regular expression match object.

        Returns:
            str: The replacement string.

        """
        self.log.info(
            "%s[%s] Replacing asciinema-player block for match %s",
            self.config.plugin_name,
            self.match_id,
            self.match_id,
        )
        parsed_json = self.parse_json(match.group(1))
        if not self.validate_config(parsed_json) or parsed_json is None:
            self.log.info(
                "%s[%s] Skipping replace",
                self.config.plugin_name,
                self.match_id,
            )
            return ""
        parsed_json["file_path"] = self.site_url + parsed_json["file"]
        parsed_json["match_id"] = self.match_id
        template = self.render_template(parsed_json)
        self.match_id += 1
        return template

    def on_page_markdown(
        self,
        markdown: str,
        page: Page,  # noqa: ARG002
        config: MkDocsConfig,  # noqa: ARG002
        files: Files,  # noqa: ARG002
    ) -> str:
        """
        Return the modified markdown page.

        This function searches for Asciinema player blocks in the markdown
        content and replaces them with the rendered template containing
        the specified Asciinema player configuration.

        Args:
            markdown (str): The markdown content of the page.
            page (Page): The current page being processed.
            config (MkDocsConfig): The MkDocs configuration object.
            files (Files): The file structure of the MkDocs project.

        Returns:
            str | None: The modified markdown content or None if no
                        modification is needed.

        """
        return re.sub(
            re.compile(r"```asciinema-player\n(.*?)\n```", re.DOTALL),
            self.replace_asciinema_player_match,
            markdown,
        )

    def on_files(self, files: Files, config: Config) -> Files:
        """
        Return the modified file structure.

        This function is responsible for copying necessary files,
        such as CSS and JavaScript files,
        required for embedding the Asciinema player in the MkDocs documentation.

        Args:
            files (Files): The file structure of the MkDocs project.
            config (MkDocsConfig): The MkDocs configuration object.

        Returns:
            Files: The modified file structure after copying additional files.

        """
        self.log.info("[mkdocs-asciinema-player] Adding assets files to the build")
        assets_src_dir = str(Path(__file__).parent / "assets")
        css_dest_dir = str(Path(config["site_dir"]) / "css")
        js_dest_dir = str(Path(config["site_dir"]) / "js")
        icons_dest_dir = str(Path(css_dest_dir) / "icons")

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
        Return the modified version of the MkDocs configuration.

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
        self.log.info(
            "%s Adding extra_css and extra_javascript to the config",
            self.config.plugin_name,
        )
        config["extra_css"].append("css/terminal-player.css")
        config["extra_css"].append("css/asciinema-player.css")
        config["extra_javascript"].append("js/asciinema-player.min.js")
        return config
