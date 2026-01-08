# Setup

---

## Configuration

### Global Usage

In your `mkdocs.yml` file, in the plugins section, you can configure the `Asciinema Player plugin` globally. Any option you set here will apply to all Asciinema Player blocks, unless overridden in an individual block:

```yaml
plugins:
  - search
  - asciinema-player:
      loglevel: "INFO"
      title: "Terminal"
      mkap_theme: "night"
      cols: 80
      rows: 24
      auto_play: false
      preload: false
      loop: false
      start_at: "0:00"
      speed: 1.0
      theme: "asciinema"
      fit: "width"
      controls: "auto"
      pause_on_markers: false
      terminal_font_size: "small"
      terminal_font_family: "Consolas"
      terminal_line_height: "1.33333333"
```

### Individual Usage

To use individual configurations, create a JSON object like the example below:

```json
{
    "file": "assets/asciinema/bootstrap.cast",
    "cols": 80,
    "auto_play": "true"
}
```

> Important: "file" is required for every individual block.

### Available Configuration Options

| Parameter                                                                                    | Default      | Scope               | Description                                                             |
| -------------------------------------------------------------------------------------------- | ------------ | ------------------- | ----------------------------------------------------------------------- |
| `loglevel`                                                                                   | "INFO"       | Global only         | Log level of the plugin ("DEBUG", "INFO", "WARNING", "ERROR", "FATAL"). |
| `title`                                                                                      | "Terminal"   | Global + Individual | Title of the terminal.                                                  |
| `mkap_theme`                                                                                 | "night"      | Global + Individual | Theme of the terminal.                                                  |
| [cols](https://docs.asciinema.org/manual/player/options/#cols)                               | 80           | Global + Individual | Number of columns in the terminal.                                      |
| [rows](https://docs.asciinema.org/manual/player/options/#rows)                               | 24           | Global + Individual | Number of rows in the terminal.                                         |
| [auto_play](https://docs.asciinema.org/manual/player/options/#autoplay)                      | false        | Global + Individual | Automatic playback upon load.                                           |
| [preload](https://docs.asciinema.org/manual/player/options/#preload)                         | false        | Global + Individual | Preload the cast file on load.                                          |
| [loop](https://docs.asciinema.org/manual/player/options/#loop)                               | false        | Global + Individual | Enable looped playback.                                                 |
| [start_at](https://docs.asciinema.org/manual/player/options/#startat)                        | "0:00"       | Global + Individual | Start playback at a specific time.                                      |
| [speed](https://docs.asciinema.org/manual/player/options/#speed)                             | 1.0          | Global + Individual | Playback speed multiplier.                                              |
| [theme](https://docs.asciinema.org/manual/player/options/#theme)                             | "asciinema"  | Global + Individual | Terminal theme for rendering.                                           |
| [fit](https://docs.asciinema.org/manual/player/options/#fit)                                 | "width"      | Global + Individual | Terminal fit mode.                                                      |
| [controls](https://docs.asciinema.org/manual/player/options/#controls)                       | "auto"       | Global + Individual | Display controls automatically.                                         |
| [pause_on_markers](https://docs.asciinema.org/manual/player/options/#pauseonmarkers)         | false        | Global + Individual | Pause playback on markers.                                              |
| [terminal_font_size](https://docs.asciinema.org/manual/player/options/#terminalfontsize)     | "small"      | Global + Individual | Font size of the terminal.                                              |
| [terminal_font_family](https://docs.asciinema.org/manual/player/options/#terminalfontfamily) | "Consolas"   | Global + Individual | Font family of the terminal.                                            |
| [terminal_line_height](https://docs.asciinema.org/manual/player/options/#terminallineheight) | "1.33333333" | Global + Individual | Line height of the terminal.                                            |

For more detailed information and additional options, refer to the [official documentation](https://docs.asciinema.org/manual/player/options/#options).
