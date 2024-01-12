# Swear Word Detection Tool

This Python script provides a simple static analysis tool that scans files for swear words. It checks all text files within the directory it's run from and all subdirectories for any matches against a predefined list of swear words.

## Features

- Recursive directory scanning
- Case-insensitive swear word matching
- Highlighting of swear words within the text
- Summary of findings with counts per file and total

## Requirements

- Python 3.x
- Terminal that supports ANSI escape sequences for colored output

## Usage

To use this tool, follow these steps:

1. Ensure you have `Python 3.x` installed on your system.
2. Place the `swear_word_checker.py` script in the root directory that you want to scan.
3. Create a `swear_words.txt` file in the same directory as the script, with one swear word per line that you wish to detect.
4. Run the script with:

```bash
python swear_word_checker.py
