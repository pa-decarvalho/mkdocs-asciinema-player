"""All tests for AsciinemaPlayerPlugin class."""
import unittest
from mkdocs.config.defaults import MkDocsConfig
from mkdocs_asciinema_player.plugin import AsciinemaPlayerPlugin


class TestAsciinemaPlayerPlugin(unittest.TestCase):
    """Test suite for the AsciinemaPlayerPlugin class."""

    def setUp(self) -> None:
        """Set up the test environment before each test method."""
        self.plugin = AsciinemaPlayerPlugin()
        self.plugin.config = MkDocsConfig()
        self.plugin.config.loglevel = "INFO"
        self.plugin.init_logging()

    def test_parse_json_correct(self) -> None:
        """
        Test JSON parsing with valid input.

        Verifies that the parse_json method correctly processes a valid JSON string
        and returns the expected dictionary with proper value types.
        """
        correct_json_str = '{ "name": "John", "age": 30, "city": "New York" }'
        expected_result = {
            "name": "John",
            "age": 30,
            "city": "New York",
        }
        result = self.plugin.parse_json(correct_json_str)
        assert result["name"] == expected_result["name"]
        assert result["age"] == expected_result["age"]
        assert result["city"] == expected_result["city"]

    def test_parse_json_incorrect(self) -> None:
        """
        Test JSON parsing with invalid input.

        Verifies that the parse_json method properly handles invalid JSON input
        by returning None instead of raising an exception.
        """
        incorrect_json_str = "hello world"
        result = self.plugin.parse_json(incorrect_json_str)
        assert result is None

    def test_render_template(self) -> None:
        """
        Test template rendering functionality.

        Verifies that the render_template method successfully processes a complete
        set of configuration data and returns a non-None result. Tests all supported
        template parameters including theme, dimensions, and playback options.
        """
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
        result = self.plugin.render_template(data)
        assert result is not None

    def test_valid_configuration(self) -> None:
        """
        Test configuration validation with valid input.

        Verifies that the validate_config method correctly accepts a valid
        configuration dictionary containing all required parameters with proper types.
        """
        user_config = {
            "file": "assets/asciinema/bootstrap.cast",
            "autoplay": True,
            "speed": 1.5,
            "theme": "dark",
        }
        assert self.plugin.validate_config(user_config) is True

    def test_missing_required_parameter(self) -> None:
        """
        Test configuration validation with missing required parameter.

        Verifies that the validate_config method correctly rejects a configuration
        dictionary that is missing the required 'file' parameter.
        """
        user_config = {
            "autoplay": True,
            "speed": 1.5,
            "theme": "dark",
        }
        assert self.plugin.validate_config(user_config) is False

    def test_required_parameter_invalid_type(self) -> None:
        """
        Test configuration validation with invalid type for required parameter.

        Verifies that the validate_config method correctly rejects a configuration
        where the required 'file' parameter is not a string.
        """
        user_config = {
            "file": 10,
            "autoplay": True,
            "speed": 1.5,
            "theme": "dark",
        }
        assert self.plugin.validate_config(user_config) is False

    def test_invalid_type(self) -> None:
        """
        Test configuration validation with invalid parameter type.

        Verifies that the validate_config method correctly rejects a configuration
        where an optional parameter ('speed') has an invalid type.
        """
        user_config = {
            "file": "assets/asciinema/bootstrap.cast",
            "speed": "test",
        }
        assert self.plugin.validate_config(user_config) is False
