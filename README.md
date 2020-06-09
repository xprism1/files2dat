# files2dat

## Introduction
Adds hashes of files in a folder to a datfile, with support for batch adding sub-entries (e.g. status="verified")

## Requirements:
- Python 3
- Beautiful Soup 4
- LXML parser

Install both with `pip install beautifulsoup4 lxml`

## How to use:
Run `files2dat.py`.

## Notes:
- Do not put the python scripts or the datfile inside the folder with files you want to add. Move them out of the folder.
- Only answer y or n to the [y/n] questions
- After script has completed, please open the datfile in a text editor, and manually remove `<html>`, `<body` (at the start of the file) as well as `</body>`, `</html>` (at the end of the file).
