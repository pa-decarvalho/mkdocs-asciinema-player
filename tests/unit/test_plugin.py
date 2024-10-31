import unittest
from mkdocs_asciinema_player.plugin import AsciinemaPlayerPlugin


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
        plugin = AsciinemaPlayerPlugin()
        data = {
            "match_id": 0,
            "file_path": "/example-group/project-name/assets/asciinema/test.cast",
            "file": "assets/asciinema/test.cast",
            "mkap_theme": "night",
            "cols": 120,
            "rows": 24,
            "auto_play": True,
            "preload": False,
            "loop": False,
            "start_at": "0:00",
            "speed": 1.0,
            "theme": "asciinema",
            "fit": "width",
            "controls": "auto",
            "pause_on_markers": False,
            "terminal_font_size": "small",
            "terminal_font_family": "Consolas",
            "terminal_line_height": "1.33333333",
        }
        result = plugin.render_template(data)
        self.assertIsNotNone(result)

    def test_valid_configuration(self) -> None:
        user_config = {
            "file": "assets/asciinema/bootstrap.cast",
            "autoplay": True,
            "speed": 1.5,
            "theme": "dark"
        }
        plugin = AsciinemaPlayerPlugin()
        self.assertTrue(plugin.validate_config(user_config))

    def test_missing_required_parameter(self) -> None:
        user_config = {
            "autoplay": True,
            "speed": 1.5,
            "theme": "dark"
        }
        plugin = AsciinemaPlayerPlugin()
        self.assertFalse(plugin.validate_config(user_config))

    def test_required_parameter_invalid_type(self) -> None:
        user_config = {
            "file": 10,
            "autoplay": True,
            "speed": 1.5,
            "theme": "dark"
        }
        plugin = AsciinemaPlayerPlugin()
        self.assertFalse(plugin.validate_config(user_config))

    def test_invalid_type(self) -> None:
        user_config = {
            "file": "assets/asciinema/bootstrap.cast",
            "speed": "test"
        }
        plugin = AsciinemaPlayerPlugin()
        self.assertFalse(plugin.validate_config(user_config))
