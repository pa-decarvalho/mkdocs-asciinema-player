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

To use `mkdocs-asciinema-player` you need to create a [fenced code block](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks) with `asciinema-player` specified as the language. The plugin detects and parses these blocks to render the Asciinema player.

First, place your [asciinema](https://asciinema.org/) `.cast` file somewhere inside your MkDocs `docs/` directory.

Then, add a fenced code block containing a minimal JSON configuration:

```json
{
  "file": "assets/asciinema/asciinema_example.cast"
}
```

**Notes**:

- The fenced code block must use `asciinema-player` as its language for the plugin to work.
- The `file` path is resolved relative to the current Markdown file location.
- The `file` value can also be a remote URL (for example, a raw file hosted online).
