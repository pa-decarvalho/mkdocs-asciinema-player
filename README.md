# mkdocs-asciinema-player

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/pa-decarvalho/mkdocs-asciinema-player)

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
