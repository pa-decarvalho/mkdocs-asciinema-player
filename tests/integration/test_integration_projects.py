import pytest
import os
import shutil
import subprocess
from bs4 import BeautifulSoup


PROJECT_PATH = os.path.join(os.path.dirname(__file__), "../fixtures/projects")


@pytest.mark.parametrize(
    "project, check",
    [
        ("simple", False),
        ("material", False),
    ],
)
class TestIntegrationProjects:
    def test_integration_project(self, project: str, check: bool) -> None:
        base_path = f"{PROJECT_PATH}/{project}"
        mkdocs_file = f"{base_path}/mkdocs.yml"
        generated_site = f"{base_path}/site"
        index_file = f"{generated_site}/index.html"

        if check:
            self.build_doc(mkdocs_file)
            self.div_asciinema_exists(index_file)
            self.delete_generated_site(generated_site)

    def build_doc(self, mkdocs_file: str) -> None:
        command = f"TZ=UTC mkdocs build -f {mkdocs_file}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        assert result.returncode == 0

    def div_asciinema_exists(self, index_file: str) -> None:
        with open(index_file, "r") as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, "html.parser")
        target_element = soup.find("div", id="clone-and-test")
        assert target_element is not None

    def delete_generated_site(self, generated_site: str) -> None:
        if os.path.exists(generated_site):
            shutil.rmtree(generated_site)
