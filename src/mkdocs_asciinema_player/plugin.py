"""
MkDocs Asciinema Player Plugin.

This module defines the AsciinemaPlayerPlugin for embedding Asciinema player in MkDocs.

Author: De Carvalho Philippe-Andre
"""
import os
import re
import json
from json import JSONDecodeError
from typing import cast, Any, Optional, Match, Dict
from urllib.parse import urlparse
from jinja2 import Environment, PackageLoader
from mkdocs.plugins import BasePlugin
from mkdocs.config.base import Config
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files, File


class AsciinemaPlayerConfig(Config):
    """
    Configuration class for the AsciinemaPlayerPlugin.
    """


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
            {"name": "terminal_font_family", "default": "Consolas"},
            {"name": "terminal_line_height", "default": "1.33333333"},
        ]
    }

    def __init__(self) -> None:
        """
        Initializes an instance of the AsciinemaPlayerPlugin.
        """
        self.mkdocs_config = MkDocsConfig()
        self.match_id = 0

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
            print(f"JSONDecodeError: {e}")
        return None

    def render_template(self, data: dict[Any, Any]) -> str:
        """
        Renders a Jinja2 template with the given data.

        Args:
            data (dict): The data to be passed to the Jinja2 template.

        Returns:
            str: The rendered template as a string.
        """
        env = Environment(
            loader=PackageLoader("mkdocs_asciinema_player", "templates"),
            lstrip_blocks=True,
            trim_blocks=True,
            autoescape=True,
        )
        return env.get_template("asciinema_player.html.j2").render(data)

    def validate_config(self, user_config: dict[str, Any]) -> bool:
        """
        Validates the user configuration for the AsciinemaPlayerPlugin.

        Args:
            user_config (dict): The user-provided configuration for the plugin.

        Returns:
            bool: True if the configuration is valid, False otherwise.
        """
        parameters = self.default_configs.get("parameters", [])

        if "file" not in user_config:
            return False

        for param in parameters:
            param = cast(Dict[str, Any], param)
            param_name = param["name"]
            param_type = type(param["default"])

            if param_name in user_config:
                user_value = user_config[param_name]
                if not isinstance(user_value, param_type):
                    return False
            elif "default" in param:
                user_config[param_name] = param["default"]

        return True

    def replace_asciinema_player_match(self, match: Match[str]) -> str:
        """
        Replaces the matched Asciinema player block with the rendered template.

        Args:
            match (re.Match): The regular expression match object.

        Returns:
            str: The replacement string.
        """
        parsed_json = self.parse_json(match.group(1))
        if not self.validate_config(parsed_json) or parsed_json is None:
            return ""
        parsed_json["file_path"] = urlparse(self.mkdocs_config["site_url"]).path + parsed_json["file"]
        parsed_json["match_id"] = self.match_id
        self.match_id += 1
        return self.render_template(parsed_json)

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
        self.mkdocs_config = config
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
        assets_src_dir = os.path.join(os.path.dirname(__file__), "assets")
        css_dest_dir = os.path.join(config["site_dir"], "css")
        js_dest_dir = os.path.join(config["site_dir"], "js")

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
        config["extra_css"].append("css/terminal-player.css")
        config["extra_css"].append("css/asciinema-player.css")
        config["extra_javascript"].append("js/asciinema-player.min.js")

        return config
