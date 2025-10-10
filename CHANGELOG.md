## 0.18.0 (2025-10-10)

### Feat

- update asciinema player to 3.11.1

## 0.17.0 (2025-04-28)

### Feat

- refactor all logging prints

## 0.16.0 (2025-02-12)

### Feat

- update asciinema player to 3.9.0 and add gitpod flex support

## 0.15.1 (2024-11-13)

### Fix

- update ruff configuration and refactor some code

## 0.15.0 (2024-11-06)

### Feat

- add penguin theme

## 0.14.0 (2024-11-02)

### Feat

- add better logging system

### Fix

- add new var default_param to be abble to print it in a f-string (below 3.12)

## 0.13.0 (2024-10-31)

### Feat

- refactor theme import system and prevent invalid theme name input

## 0.12.0 (2024-10-31)

### Feat

- add none theme

## 0.11.0 (2024-10-26)

### Feat

- update asciinema-player to 3.8.1

## 0.10.1 (2024-08-07)

### Fix

- allow to use mkdocs site_url var with e-default None value

## 0.10.0 (2024-07-22)

### Feat

- update asciinema-player version to 3.8.0

## 0.9.0 (2024-06-05)

### Feat

- improved blue theme buttons

## 0.8.2 (2024-05-21)

### Fix

- add fonts and icons to manifest file

## 0.8.1 (2024-03-28)

### Fix

- fix pypi action workflow

## 0.8.0 (2024-03-28)

### Feat

- add default theme fonts and refactor code
- add terminal themes

### Fix

- change theme var name to mkap_theme

## 0.7.1 (2024-03-22)

### Fix

- center window title with buttons

## 0.7.0 (2024-01-24)

### Feat

- add validate user config feature

## 0.6.1 (2023-12-21)

### Fix

- **plugin**: resolve issue with boolean types not being handled properly

## 0.6.0 (2023-12-21)

### Feat

- **css**: add a border and box-shadow to mkap-window

## 0.5.0 (2023-12-20)

### Feat

- rework the look of the terminal and add title parameter

## 0.4.3 (2023-12-19)

### Fix

- resolve issue with multiple terminals not appearing on the same page

## 0.4.2 (2023-12-19)

### Fix

- **plugin**: modify file copying mechanism for CSS and JS assets

## 0.4.1 (2023-12-18)

### Fix

- change on_pre_build event to on_files to prevent doc from looping on build

## 0.4.0 (2023-12-15)

### Feat

- create feature to change description in pypi

## 0.3.0 (2023-12-15)

### Feat

- add manifest to push to pypi

## 0.2.0 (2023-12-15)

### Feat

- test add release

## 0.1.0 (2023-12-15)

### Feat

- adcustom css file
- add params for asciinema-player
- change requires-python var to >= 3.9
- add on_pre_build callback for automatic inclusion of asciinema css and js to doc
- refactor project
- add on_page_markdown event and start new functional test
- add plugin base class
- add base project with AsciinemaPlayerPlugin class and settings

### Refactor

- add lint and test taskfiles and refactor project
