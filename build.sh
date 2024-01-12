#!/bin/sh
echo "##active_line2##"

echo "##active_line3##"
pip install -r requirements.txt
echo "##active_line4##"
pyinstaller --onefile main.py
