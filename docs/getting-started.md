# Getting Started

---

## Installation

To begin, install the `mkdocs-asciinema-player` package by executing the following command in the command line:

```sh
pip install mkdocs-asciinema-player
```

## Configuration

In your `mkdocs.yml` file, include `asciinema-player` in the plugins section as follows:

```yaml
plugins:
  - search
  - asciinema-player
```

## Usage

To use `mkdocs-asciinema-player` you need to create a [fenced code block](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks) with `asciinema-player` specified as the language.

Within your MkDocs documentation folder, add any  [asciinema](https://asciinema.org/) `.cast` file and insert the following minimal JSON inside your fenced code block:

TODO: Add example (not working because the plugin parses it; refer to the [README](https://github.com/pa-decarvalho/mkdocs-asciinema-player/blob/main/README.md) for an example)
