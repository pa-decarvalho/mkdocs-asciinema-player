"""
MkDocs Asciinema Player Plugin.

This module defines the AsciinemaPlayerPlugin for embedding Asciinema player in MkDocs.

Author: De Carvalho Philippe-Andre
"""
import os
import shutil
import re
import json
from json import JSONDecodeError
from typing import Any, Optional, Match
from urllib.parse import urlparse
from jinja2 import Environment, PackageLoader
from mkdocs.plugins import BasePlugin
from mkdocs.config.base import Config
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files


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
        replace_asciinema_player_match: Replaces the matched Asciinema player block with the rendered template.
        on_page_markdown: Callback function called when processing page markdown.
    """
    def __init__(self) -> None:
        self.mkdocs_config = MkDocsConfig()

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

    def replace_asciinema_player_match(self, match: Match[str]) -> str:
        """
        Replaces the matched Asciinema player block with the rendered template.

        Args:
            match (re.Match): The regular expression match object.
        Returns:
            str: The replacement string.
        """
        parsed_json = self.parse_json(match.group(1))
        if parsed_json is None:
            return ""
        parsed_json["site_url"] = urlparse(self.mkdocs_config["site_url"]).path
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
        print(config)
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
        required for embedding the Asciinema player in the MkDocs documentation. It also updates
        the MkDocs configuration to include the copied files.

        Args:
            files (Files): The file structure of the MkDocs project.
            config (Config): The MkDocs configuration object.

        Returns:
            Files: The modified file structure after copying additional files.
        """
        # Copy custom terminal player CSS file
        terminal_player_css_file = os.path.join(os.path.dirname(__file__), "assets", "terminal-player.css")
        dest_terminal_player_css_file = os.path.join(config["docs_dir"], "assets", "css", "terminal-player.css")
        os.makedirs(os.path.dirname(dest_terminal_player_css_file), exist_ok=True)
        shutil.copyfile(terminal_player_css_file, dest_terminal_player_css_file)

        # Copy Asciinema CSS file
        asciinema_css_file = os.path.join(os.path.dirname(__file__), "assets", "asciinema-player.css")
        dest_asciinema_css_file = os.path.join(config["docs_dir"], "assets", "css", "asciinema-player.css")
        os.makedirs(os.path.dirname(dest_asciinema_css_file), exist_ok=True)
        shutil.copyfile(asciinema_css_file, dest_asciinema_css_file)

        # Copy Asciinema JavaScript file
        asciinema_js_file = os.path.join(os.path.dirname(__file__), "assets", "asciinema-player.min.js")
        dest_asciinema_js_file = os.path.join(config["docs_dir"], "assets", "js", "asciinema-player.min.js")
        os.makedirs(os.path.dirname(dest_asciinema_js_file), exist_ok=True)
        shutil.copyfile(asciinema_js_file, dest_asciinema_js_file)

        # Update MkDocs configuration to include the copied files
        config["extra_css"].append("assets/css/terminal-player.css")
        config["extra_css"].append("assets/css/asciinema-player.css")
        config["extra_javascript"].append("assets/js/asciinema-player.min.js")

        # Return the modified file structure
        return files
