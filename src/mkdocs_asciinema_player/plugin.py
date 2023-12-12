"""
MkDocs Asciinema Player Plugin.

This module defines the AsciinemaPlayerPlugin for embedding Asciinema player in MkDocs.

Author: De Carvalho Philippe-Andre
"""
import re
import json
from json import JSONDecodeError
from typing import Any, Optional, Match
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
        return env.get_template("asciinema_player.html").render(data)

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
        template_data = {
            "site_url": self.mkdocs_config["site_url"],
            "cast_file_path": parsed_json["cast_file_path"]
        }
        return self.render_template(template_data)

    # pylint: disable-next=unused-argument
    def on_page_markdown(self, markdown: str, page: Page, config: MkDocsConfig, files: Files) -> Optional[str]:
        """
        Callback function called when processing page markdown.

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
