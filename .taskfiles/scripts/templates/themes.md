# Themes

{% for theme in themes -%}
## {{ theme|capitalize }} Theme

```asciinema-player
{
    "file": "../assets/asciinema/asciinema_example.cast",
    "mkap_theme": "{{ theme }}",
    "auto_play": true
}
```

Example:

```json
{
    "file": "assets/asciinema/asciinema_example.cast",
    "mkap_theme": "{{ theme }}",
    "auto_play": true
}
```

{% endfor -%}
