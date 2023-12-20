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
            expected_file_content = file.read()
        self.expected_data = expected_file_content
        plugin = AsciinemaPlayerPlugin()
        data = {
            "match_id": 0,
            "site_url": "/example-group/project-name/",
            "file": "assets/asciinema/test.cast",
            "cols": 120,
            "auto_play": "true"
        }
        result = plugin.render_template(data)
        self.assertEqual(result, self.expected_data)

    def test_replace_asciinema_player(self) -> None:
        with open(TESTDATA_EXPECTED_DATA_FILE, "r") as file:
            expected_file_content = file.read()
        markdown_example = "```asciinema-player\n{\"file\": \"assets/asciinema/test.cast\", \"cols\": 120, \"auto_play\": \"true\"}\n```"
        match_example = re.match(r"```asciinema-player\n(.*?)\n```", markdown_example)
        plugin = AsciinemaPlayerPlugin()
        setattr(plugin, "mkdocs_config", {"site_url": "https://localhost:8000/example-group/project-name/"})
        print(plugin)
        self.assertEqual(plugin.replace_asciinema_player_match(match_example), expected_file_content)
