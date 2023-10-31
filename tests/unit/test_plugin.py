import unittest
import os
from mkdocs_asciinema_player.plugin import AsciinemaPlayerPlugin


TESTDATA_EXPECTED_DATA_FILE = os.path.join(os.path.dirname(__file__), "data/expected_data.md")


class TestAsciinemaPlayerPlugin(unittest.TestCase):
    def setUp(self):
        with open(TESTDATA_EXPECTED_DATA_FILE, "r") as file:
            file_content = file.read()
        self.site_url = "https://localhost/example-group/project-name"
        self.src_file = "test.cast"
        self.expected_data = file_content

    def test_asciinema_player(self) -> None:
        plugin = AsciinemaPlayerPlugin()
        self.assertEqual(plugin.asciinema_player(self.site_url, self.src_file), self.expected_data)
