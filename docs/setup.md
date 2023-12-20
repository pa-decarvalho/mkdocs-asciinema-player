# Setup

---

## Configuration

### Global Usage

*Coming soon...*

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

|                                                  Parameter                                                  |    Value     |            Description             |
| ----------------------------------------------------------------------------------------------------------- | ------------ | ---------------------------------- |
| file                                                                                                        | -            | Path to the cast file.             |
| title                                                                                                       | "Terminal"   | Title of the terminal.             |
| [cols](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#cols)                               | 80           | Number of columns in the terminal. |
| [rows](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#rows)                               | 24           | Number of rows in the terminal.    |
| [auto_play](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#autoplay)                      | false        | Automatic playback upon load.      |
| [preload](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#preload)                         | false        | Preload the cast file on load.     |
| [loop](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#loop)                               | false        | Enable looped playback.            |
| [start_at](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#startat)                        | 0            | Start playback at a specific time. |
| [speed](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#speed)                             | 1            | Playback speed multiplier.         |
| [theme](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#theme)                             | "asciinema"  | Terminal theme for rendering.      |
| [fit](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#fit)                                 | "width"      | Terminal fit mode.                 |
| [controls](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#controls)                       | "auto"       | Display controls automatically.    |
| [pause_on_markers](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#pauseonmarkers)         | false        | Pause playback on markers.         |
| [terminal_font_size](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#terminalfontsize)     | "small"      | Font size of the terminal.         |
| [terminal_font_family](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#terminalfontfamily) | "Consolas"   | Font family of the terminal.       |
| [terminal_line_height](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#terminallineheight) | "1.33333333" | Line height of the terminal.       |

For more detailed information and additional options, refer to the [official documentation](https://github.com/asciinema/asciinema-player?tab=readme-ov-file#options).
