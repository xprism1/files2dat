# files2dat

## Introduction
Adds hashes of files in a folder to a datfile, with support for batch adding sub-entries for those files (e.g. status="verified")

## Requirements:
- Python 3
- Beautiful Soup 4
- LXML parser

Install both with `pip install beautifulsoup4 lxml`

## How to use:
Run `main.py`.

## Notes:
- Do not put the python scripts or the datfile inside the folder with files you want to add. Move them out of the folder.
- Remove the `__pycache` folder before executing the script
- Only answer y or n to the [y/n] questions
