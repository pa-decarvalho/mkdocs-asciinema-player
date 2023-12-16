# mkdocs-asciinema-player

[![documentation](https://img.shields.io/badge/docs-mkdocs--asciinema--player-blue.svg?style=flat)](https://pa-decarvalho.github.io/mkdocs-asciinema-player/)
[![test](https://github.com/pa-decarvalho/mkdocs-asciinema-player/workflows/test/badge.svg)](https://github.com/pa-decarvalho/mkdocs-asciinema-player/actions)
[![pypi](https://img.shields.io/pypi/v/mkdocs-asciinema-player.svg)](https://pypi.org/project/mkdocs-asciinema-player/)
[![downloads](https://img.shields.io/pypi/dm/mkdocs-asciinema-player.svg)](https://pypi.org/project/mkdocs-asciinema-player/)

A Mkdocs Plugin to include asciinema player in your documentation.

## Setup

Install the plugin via pip :

```sh
pip install mkdocs-asciinema-player
```

## Configure

In your mkdocs.yml, add `asciinema-player` to the `plugins` section :

```yaml
plugins:
  - search
  - asciinema-player
```

In your `.gitignore` file, add this part to ignore copied files :

```sh
# Auto generated assets
docs/assets/css
docs/assets/js
```

## Usage

In your MkDocs docs folder, add any [asciinema](https://asciinema.org/) `.cast` file and add this to any markdown page :

````markdown
```asciinema-player
{
    "cast_file_path": "assets/asciinema/bootstrap.cast"
}
```
````
