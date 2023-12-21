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
