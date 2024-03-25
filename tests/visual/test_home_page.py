from base_case_test import BaseMkDocsTest


class HomePageTest(BaseMkDocsTest):
    def test_homepage(self):
        self.open(self.mkdocs_serve_url)

        # Assert title
        self.assert_title("Test MkDocs asciinema-player plugin")
        self.assert_exact_text("Test MkDocs Asciinema Player", "h1")
