# mkdocs-asciinema-player

[![gitpod-ready-to-code](https://img.shields.io/badge/gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/pa-decarvalho/mkdocs-asciinema-player)
[![test](https://github.com/pa-decarvalho/mkdocs-asciinema-player/workflows/test/badge.svg)](https://github.com/pa-decarvalho/mkdocs-asciinema-player/actions)
[![pypi](https://img.shields.io/pypi/v/mkdocs-asciinema-player.svg)](https://pypi.org/project/mkdocs-asciinema-player/)
[![pyversions](https://img.shields.io/pypi/pyversions/mkdocs-asciinema-player.svg)](https://pypi.python.org/pypi/mkdocs-asciinema-player)
[![downloads](https://img.shields.io/pypi/dm/mkdocs-asciinema-player.svg)](https://pypi.org/project/mkdocs-asciinema-player/)
[![license](https://img.shields.io/pypi/l/mkdocs-asciinema-player.svg)](https://pypi.python.org/pypi/mkdocs-asciinema-player)

A Mkdocs Plugin to include asciinema player in your documentation.

## Related Projects

| Name                                                                                            | Description                                                            |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [98.css](https://github.com/jdan/98.css)                                                        | 98.css from [jdan](https://github.com/jdan)                            |

## Quick Setup

### Installation

Install the plugin via pip :

```sh
pip install mkdocs-asciinema-player
```

### Configure

In your `mkdocs.yml`, add `asciinema-player` to the `plugins` section :

```yaml
plugins:
  - search
  - asciinema-player
```

### Usage

In your MkDocs docs folder, add any [asciinema](https://asciinema.org/) `.cast` file and add this to any markdown page :

````markdown
```asciinema-player
{
    "file": "assets/asciinema/bootstrap.cast"
}
```
````

### More

For more information on the plugin, you can visit the the following [website](https://pa-decarvalho.github.io/mkdocs-asciinema-player/)

You will find the complete documentation of the plugin, examples of use, installation and configuration instructions.

## Contributing

See [CONTRIBUTING.md](https://github.com/pa-decarvalho/mkdocs-asciinema-player/blob/main/CONTRIBUTING.md) file.
