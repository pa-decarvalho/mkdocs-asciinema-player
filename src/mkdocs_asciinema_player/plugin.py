import re
from typing import Match
from jinja2 import Environment, PackageLoader, Template
from urllib.parse import urlparse
from mkdocs.plugins import BasePlugin
from mkdocs_asciinema_player.utils import Utils


class AsciinemaPlayerPlugin(BasePlugin):
    def __init__(self) -> None:
        pass

    def replace_asciinema_player_match(self, match: Match[str]) -> str:
        utils = Utils()
        parsed_json = utils.parse_json(match.group(1))
        if parsed_json is None:
            return ""
        template_data = {
            "site_url": self.mkdocs_config["site_url"],
            "cast_file_path": parsed_json["cast_file_path"]
        }
        return utils.render_template(template_data)

    def on_page_markdown(self, markdown: str, config, **kwargs) -> str:
        self.mkdocs_config = config
        return re.sub(
            re.compile(r"```asciinema-player\n(.*?)\n```", re.DOTALL),
            self.replace_asciinema_player_match,
            markdown
        )
