# Contributing

Thank you for considering contributing to the **mkdocs-asciinema-player** project! We appreciate your time and effort in helping to make this project better.

## Table of Contents

- [How Can I Contribute?](#how-can-i-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Enhancements](#suggesting-enhancements)
    - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
    - [Using Gitpod](#using-gitpod)
    - [Local Development](#local-development)
- [Project Guidelines](#project-guidelines)
    - [Coding Standards](#coding-standards)
    - [Creating Themes](#creating-themes)
- [License](#license)

## How Can I Contribute?

### Reporting Bugs

- Create an issue on our [GitHub Issues](https://github.com/pa-decarvalho/mkdocs-asciinema-player/issues) page
- Provide detailed information about:
    - Steps to reproduce the bug
    - Expected behavior
    - Actual behavior
    - Environment details (OS, browser, etc.)

### Suggesting Enhancements

- Open an issue on our [GitHub Issues](https://github.com/pa-decarvalho/mkdocs-asciinema-player/issues) page
- Clearly describe:
    - The proposed enhancement
    - Why it would be useful
    - How it should work

### Pull Requests

Follow these steps to submit your contributions:

- Fork the repository to your GitHub account
- Clone your fork:

```sh
git clone https://github.com/your-username/mkdocs-asciinema-player.git
```

- Create a new branch:

```sh
git checkout -b feature/your-feature-name
```

- Make and commit your changes:

```sh
git add . && git commit -m "feat: my new feature"
```

- Push your branch:

```sh
git push origin feature/your-feature-name
```

- Open a Pull Request on the main repository

> **Note**: Please use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for your commit messages.

## Development Setup

### Using Gitpod

- Read the [Getting Started Guide](https://www.gitpod.io/docs/introduction/getting-started) from Gitpod
- Open your forked project in Gitpod

### Local Development

Prerequisites:

- Python >= 3.9
- [Task](https://taskfile.dev/) >= 3.45.4

Setup steps:

- Clone your fork:

```sh
git clone https://github.com/your-username/mkdocs-asciinema-player.git
```

- Run the bootstrap command:

```sh
task bootstrap
```

## Project Guidelines

### Coding Standards

- Follow PEP 8 for Python code
- Write clear and descriptive commit messages using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- Include tests for new functionality
- Keep documentation up-to-date
- Ensure all tests pass before submitting PR

### Creating Themes

To create a new theme for the asciinema player:

- Create a `<my-new-theme>.html` file in:

```sh
src/mkdocs_asciinema_player/templates/themes
```

- Add CSS styles in the `src/mkdocs_asciinema_player/assets/terminal-player.css` file, keeping the styles ordered alphabetically by theme name.

- Update documentation:

```sh
task update:docs
```

## License

By contributing, you agree that your contributions will be licensed under the project's [MIT License](https://github.com/pa-decarvalho/mkdocs-asciinema-player/blob/main/LICENSE).
