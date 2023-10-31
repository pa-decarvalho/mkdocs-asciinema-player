from jinja2 import Environment, PackageLoader, Template
from urllib.parse import urlparse
from mkdocs.plugins import BasePlugin


class AsciinemaPlayerPlugin(BasePlugin):
    def __init__(self) -> None:
        pass

    def asciinema_player(self, src_file: str) -> str:
        parsed_url = urlparse(self.config["site_url"])
        env = Environment(
            loader=PackageLoader("mkdocs_asciinema_player", "templates"),
            lstrip_blocks=True,
            trim_blocks=True,
        )
        template = env.get_template("asciinema_player.j2")
        return template.render(url=parsed_url.path, cast_file=src_file)

    def on_page_markdown(self, markdown: str, config, **kwargs) -> str:
        """
        Render the markdown content using the Jinja2 template engine.
        """
        self.config = config
        return Template(markdown).render(asciinema_player=self.asciinema_player)
