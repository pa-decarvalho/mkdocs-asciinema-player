import json
from json import JSONDecodeError
from jinja2 import Environment, PackageLoader
from typing import Any


class Utils:
    def __init__(self) -> None:
        pass

    def parse_json(self, content: str) -> Any:
        try:
            return json.loads(content)
        except JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
        return None

    def render_template(self, data: dict[Any, Any]) -> str:
        env = Environment(
            loader=PackageLoader("mkdocs_asciinema_player", "templates"),
            lstrip_blocks=True,
            trim_blocks=True,
            autoescape=True,
        )
        return env.get_template("asciinema_player.html").render(data)
