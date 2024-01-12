import os
import re
import sys
# from yaspin import yaspin
# import random
# import time

# ANSI color codes for formatting
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
CYAN = '\033[96m'
GREEN = '\033[92m'

# Support all basic termcolor text colors
colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
# List of spinners
spinners = ['dots', 'dots2', 'dots3', 'dots4', 'dots5', 'dots6', 'dots7', 'dots8', 'dots9', 'dots10', 'dots11', 'dots12']


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    # full_path = os.path.join(base_path, relative_path)
    # print(f"Resolved path: {full_path}")
    # print(f"Does file exist: {os.path.exists(full_path)}")
    return os.path.join(base_path, relative_path)


def load_swear_words(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().lower() for line in file.readlines()]

def find_swear_words(file_path, swear_words):
    matches_found = 0
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, 1):
        for swear_word in swear_words:
            if swear_word in line.lower():
                matches_found += 1
                highlighted_line = re.sub(f'({swear_word})', RED + BOLD + r'\1' + ENDC, line, flags=re.IGNORECASE)
                relative_path = os.path.relpath(file_path, start='.')
                print(f'{CYAN}{relative_path}{ENDC}:{BOLD}{line_number}{ENDC}: {highlighted_line.strip()}')

    if matches_found:
        print(f'\n  {GREEN}{matches_found} {"offender" if matches_found == 1 else "offenders"} found in {os.path.basename(file_path)}{ENDC}\n')
    return matches_found

def scan_directory(directory, swear_words):
    ignored_dirs_file = resource_path('resources/ignored_dirs.txt')
    ignored_file_types_file = resource_path('resources/ignored_file_types.txt')
    
    with open(ignored_dirs_file, 'r') as f:
        ignored_dirs = [line.strip() for line in f]
    with open(ignored_file_types_file, 'r') as f:
        ignored_file_types = [line.strip() for line in f]

    total_matches = 0
    # with yaspin() as sp:
    for root, _, files in os.walk(directory):
        if any(ignored_dir in root for ignored_dir in ignored_dirs):
            continue

        for file in files:
            if any(file.endswith(file_type) for file_type in ignored_file_types):
                continue

            file_path = os.path.join(root, file)
            matches_found = find_swear_words(file_path, swear_words)
            total_matches += matches_found
            # color = random.choice(colors)
            # spinner = random.choice(spinners)
            # sp.spinner, sp.color, sp.text = spinner, color, f"Scanning {root}"

    if total_matches:
        print(f'{BOLD}{total_matches} offenders found in total{ENDC}')

def main():
    print('')
    swear_words_file = resource_path('resources/swear_words.txt')
    swear_words = load_swear_words(swear_words_file)
    
    if not swear_words:
        print(f"No swear words loaded from {swear_words_file}. Please check the file.")
        return

    scan_directory('.', swear_words)

if __name__ == "__main__":
    main()
