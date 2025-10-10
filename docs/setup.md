# Setup

---

## Configuration

### Global Usage

In your `mkdocs.yml` file, in the `plugins` section, you can use variables ([Using plugins](https://www.mkdocs.org/dev-guide/plugins/#using-plugins)):

```yaml
plugins:
  - search
  - asciinema-player:
      myvar: "example"
```

Below is a table of available variables:

|  Parameter  |  Value  |                               Description                               |
| ----------- | ------- | ----------------------------------------------------------------------- |
|  loglevel   | "INFO"  | Log level of the plugin ("DEBUG", "INFO", "WARNING", "ERROR", "FATAL"). |

### Individual Usage

To use individual configurations, create a JSON object like the example below:

```json
{
    "file": "assets/asciinema/bootstrap.cast",
    "cols": 80,
    "auto_play": "true"
}
```

Below is a table of available configuration parameters:

|                                                  Parameter                                   |    Value     |            Description             |
| -------------------------------------------------------------------------------------------- | ------------ | ---------------------------------- |
| file                                                                                         | -            | Path to the cast file.             |
| title                                                                                        | "Terminal"   | Title of the terminal.             |
| mkap_theme                                                                                   | "night"      | Theme of the terminal.             |
| [cols](https://docs.asciinema.org/manual/player/options/#cols)                               | 80           | Number of columns in the terminal. |
| [rows](https://docs.asciinema.org/manual/player/options/#rows)                               | 24           | Number of rows in the terminal.    |
| [auto_play](https://docs.asciinema.org/manual/player/options/#autoplay)                      | false        | Automatic playback upon load.      |
| [preload](https://docs.asciinema.org/manual/player/options/#preload)                         | false        | Preload the cast file on load.     |
| [loop](https://docs.asciinema.org/manual/player/options/#loop)                               | false        | Enable looped playback.            |
| [start_at](https://docs.asciinema.org/manual/player/options/#startat)                        | 0            | Start playback at a specific time. |
| [speed](https://docs.asciinema.org/manual/player/options/#speed)                             | 1            | Playback speed multiplier.         |
| [theme](https://docs.asciinema.org/manual/player/options/#theme)                             | "asciinema"  | Terminal theme for rendering.      |
| [fit](https://docs.asciinema.org/manual/player/options/#fit)                                 | "width"      | Terminal fit mode.                 |
| [controls](https://docs.asciinema.org/manual/player/options/#controls)                       | "auto"       | Display controls automatically.    |
| [pause_on_markers](https://docs.asciinema.org/manual/player/options/#pauseonmarkers)         | false        | Pause playback on markers.         |
| [terminal_font_size](https://docs.asciinema.org/manual/player/options/#terminalfontsize)     | "small"      | Font size of the terminal.         |
| [terminal_font_family](https://docs.asciinema.org/manual/player/options/#terminalfontfamily) | "Consolas"   | Font family of the terminal.       |
| [terminal_line_height](https://docs.asciinema.org/manual/player/options/#terminallineheight) | "1.33333333" | Line height of the terminal.       |

For more detailed information and additional options, refer to the [official documentation](https://docs.asciinema.org/manual/player/options/#options).
