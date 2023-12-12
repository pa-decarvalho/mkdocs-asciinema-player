import unittest
import os
from mkdocs_asciinema_player.utils import Utils


TESTDATA_EXPECTED_DATA_FILE = os.path.join(os.path.dirname(__file__), "data/expected_data.md")


class TestUtils(unittest.TestCase):
    def test_parse_json_correct(self) -> None:
        correct_json_str = "{ \"name\": \"John\", \"age\": 30, \"city\": \"New York\" }"
        utils = Utils()
        result = utils.parse_json(correct_json_str)
        self.assertEqual(result["name"], "John")
        self.assertEqual(result["age"], 30)
        self.assertEqual(result["city"], "New York")

    def test_parse_json_incorrect(self) -> None:
        incorrect_json_str = "hello world"
        utils = Utils()
        result = utils.parse_json(incorrect_json_str)
        self.assertIsNone(result)

    def test_render_template(self) -> None:
        with open(TESTDATA_EXPECTED_DATA_FILE, "r") as file:
            file_content = file.read()
        self.expected_data = file_content
        utils = Utils()
        data = {
            "site_url": "https://localhost:8000/example-group/project-name/",
            "cast_file_path": "assets/asciinema/test.cast"
        }
        result = utils.render_template(data)
        self.assertEqual(result, self.expected_data)
