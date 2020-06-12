# files2dat

## Introduction
Adds hashes of files in a folder to a datfile, with support for batch adding sub-entries for those files (e.g. status="verified")

## Requirements:
- Python 2 and 3
- Beautiful Soup 4
- LXML parser

Install both with `pip install beautifulsoup4 lxml`
If you are on Windows, replace `C:\\Python27\\python.exe` in line 94 with the path to the Python 2 executable. Remember to use double backslash.

## How to use:
Run `main.py`.

## Notes:
- Do not put the python scripts or the datfile inside the folder with files you want to add. Move them out of the folder.
- Remove the `__pycache__` folder before executing the script
- Move the <header> section from the bottom to the top of the sorted file
