"""Update dependencies script."""

import re
import shutil
import tempfile
from pathlib import Path
from typing import Any

import requests
import yaml
from packaging import version


class DependencyManager:
    """Update all the project dependencies."""

    def __init__(self) -> None:
        """
        Initialize the DependencyManager with default configuration.

        Sets up the config file path, timeout duration,
        and loads the initial configuration.
        """
        self.config_file = Path(".config/dependencies.yml")
        self.timeout = 30  # Timeout in seconds for HTTP requests
        self.config = self.__read_config()

    def __read_config(self) -> Any:
        try:
            if self.config_file.exists():
                with Path(self.config_file).open() as f:
                    return yaml.safe_load(f)
            else:
                return {}
        except yaml.YAMLError as e:
            print(f"Error reading YAML config: {e}")
            return {}

    def __save_config(self, config: dict[Any, Any]) -> None:
        self.config_file.parent.mkdir(exist_ok=True)
        with Path(self.config_file).open("w") as f:
            yaml.safe_dump(config, f, sort_keys=False, explicit_start=True)

    def __get_latest_release(self, repo_path: str) -> Any:
        url = f"https://api.github.com/repos/{repo_path}/releases/latest"

        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()["tag_name"].lstrip("v")
        except requests.exceptions.RequestException as e:
            print(f"Error while fetching latest version for {repo_path}: {e}")
            return None

    def __update_files(
        self,
        update_files: list[str],
        current_version: str,
        latest_version: str,
    ) -> None:
        for filepath in update_files:
            file = Path(filepath)
            if file.exists():
                print(file)
                content = file.read_text()
                updated_content = re.sub(current_version, latest_version, content)
                file.write_text(updated_content)

    def __download_assets(
        self,
        download_assets: dict[Any, Any],
        repo_path: str,
        version: str,
    ) -> None:
        if not download_assets:
            return
        url = f"https://github.com/{repo_path}/releases/download/v{version}"
        path = download_assets["path"]
        files = download_assets["files"]
        try:
            with tempfile.TemporaryDirectory(
                prefix="asciinema-player-download-",
            ) as temp_dir:
                temp_path = Path(temp_dir)
                for filename in files:
                    response = requests.get(
                        url + "/" + filename,
                        stream=True,
                        timeout=self.timeout,
                    )
                    response.raise_for_status()
                    file_path = temp_dir + "/" + filename
                    with Path(file_path).open("wb") as f:
                        for chunk in response.iter_content(chunk_size=8192):  # noqa: FURB122
                            f.write(chunk)
                assets_path = Path(path)
                for filename in files:
                    old_file = assets_path / filename
                    if old_file.exists():
                        old_file.unlink()
                for filename in files:
                    shutil.copy2(temp_path / filename, assets_path / filename)
        except Exception as e:
            print(f"Error download assets: {e}")
            return

    def check_and_update(self) -> None:
        """Check if a new version if available and update files."""
        dependencies = self.config.get("dependencies", {})
        for item in dependencies:
            repo = dependencies.get(item, {}).get("repo")
            current_version = dependencies.get(item, {}).get("version")
            update_files = dependencies.get(item, {}).get("update_files")
            download_assets = dependencies.get(item, {}).get("download_assets", {})
            latest_version = self.__get_latest_release(repo)

            if version.parse(latest_version) > version.parse(current_version):
                print(f"New version {latest_version} for {item}")
                self.__update_files(update_files, current_version, latest_version)
                self.__download_assets(download_assets, repo, latest_version)
                new_config = self.__read_config()
                new_config["dependencies"][item] = {
                    "repo": repo,
                    "version": latest_version,
                    "update_files": update_files,
                    "download_assets": download_assets,
                }
                self.__save_config(new_config)


def main() -> None:
    """Run check_and_update method."""
    dependency_manager = DependencyManager()
    dependency_manager.check_and_update()


if __name__ == "__main__":
    main()
