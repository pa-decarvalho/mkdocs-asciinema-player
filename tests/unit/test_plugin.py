import unittest
import os
import re
from mkdocs_asciinema_player.plugin import AsciinemaPlayerPlugin


TESTDATA_EXPECTED_DATA_FILE = os.path.join(os.path.dirname(__file__), "data/expected_data.md")


class TestAsciinemaPlayerPlugin(unittest.TestCase):
    def test_parse_json_correct(self) -> None:
        correct_json_str = "{ \"name\": \"John\", \"age\": 30, \"city\": \"New York\" }"
        plugin = AsciinemaPlayerPlugin()
        result = plugin.parse_json(correct_json_str)
        self.assertEqual(result["name"], "John")
        self.assertEqual(result["age"], 30)
        self.assertEqual(result["city"], "New York")

    def test_parse_json_incorrect(self) -> None:
        incorrect_json_str = "hello world"
        plugin = AsciinemaPlayerPlugin()
        result = plugin.parse_json(incorrect_json_str)
        self.assertIsNone(result)

    def test_render_template(self) -> None:
        with open(TESTDATA_EXPECTED_DATA_FILE, "r") as file:
            file_content = file.read()
        self.expected_data = file_content
        plugin = AsciinemaPlayerPlugin()
        data = {
            "site_url": "https://localhost:8000/example-group/project-name/",
            "cast_file_path": "assets/asciinema/test.cast"
        }
        result = plugin.render_template(data)
        self.assertEqual(result, self.expected_data)

    def test_replace_asciinema_player(self) -> None:
        with open(TESTDATA_EXPECTED_DATA_FILE, "r") as file:
            file_content = file.read()
        self.expected_data = file_content
        markdown_example = "```asciinema-player\n{\"cast_file_path\": \"assets/asciinema/test.cast\"}\n```"
        match_example = re.match(r"```asciinema-player\n(.*?)\n```", markdown_example)
        print(match_example)
        plugin = AsciinemaPlayerPlugin()
        setattr(plugin, "mkdocs_config", {"site_url": "https://localhost:8000/example-group/project-name/"})
        print(plugin)
        self.assertEqual(plugin.replace_asciinema_player_match(match_example), self.expected_data)
