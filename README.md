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
- Only answer y or n to the [y/n] questions
- If your path has a backslash, replace it with 2 backslashes (e.g. `C:\\Users` instead of `C:\Users`)
- After script has completed, please open the datfile in a text editor, and manually remove <html> (at the start of the file) as well as </html> (at the end of the file).
