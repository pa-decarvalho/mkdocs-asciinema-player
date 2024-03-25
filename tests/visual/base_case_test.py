import subprocess
import time
from seleniumbase import BaseCase


class BaseMkDocsTest(BaseCase):
    mkdocs_dev_addr = "localhost:8002"
    mkdocs_serve_url = f"http://{mkdocs_dev_addr}"
    mkdocs_default_config = "tests/fixtures/test_doc/mkdocs_default.yml"
    mkdocs_override_config = "tests/fixtures/test_doc/mkdocs_override.yml"

    def setUp(self, override_config=False):
        super().setUp()

        if override_config:
            config_file = self.mkdocs_override_config
        else:
            config_file = self.mkdocs_default_config

        self.mkdocs_process = subprocess.Popen([
                "mkdocs", "serve",
                "--dev-addr", self.mkdocs_dev_addr,
                "--config-file", config_file
            ]
        )
        time.sleep(1)

    def tearDown(self):
        super().tearDown()
        self.mkdocs_process.terminate()

    def reload(self, override_config=False):
        self.tearDown()
        self.setUp(override_config)
