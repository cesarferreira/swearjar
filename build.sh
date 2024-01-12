#!/bin/sh

pip install -r requirements.txt
pyinstaller --onefile swearjar.py
