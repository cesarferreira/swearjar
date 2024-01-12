#!/bin/sh

pip install -r requirements.txt
pyinstaller --onefile --add-data 'resources/:.' swearjar.py
