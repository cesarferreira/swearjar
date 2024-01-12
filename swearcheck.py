import os
import re

# ANSI color codes for formatting
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
CYAN = '\033[96m'
GREEN = '\033[92m'

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
        print(f'\n  {GREEN}{matches_found} {"offender" if matches_found == 1 else "offenders"} found in {os.path.basename(file_path)}.{ENDC}\n')
    return matches_found

def scan_directory(directory, swear_words, ignored_dirs=None, ignored_file_types=None):
    if ignored_dirs is None:
        ignored_dirs = ['.git', '.dart_tool', '.idea', '.vscode', 'build', 'node_modules', 'venv', 'dist']
    if ignored_file_types is None:
        ignored_file_types = ['.zip', '.rar', '.ipa', '.mobileprovision']

    total_matches = 0

    for root, _, files in os.walk(directory):
        if any(ignored_dir in root for ignored_dir in ignored_dirs):
            continue

        for file in files:
            if any(file.endswith(file_type) for file_type in ignored_file_types):
                continue

            file_path = os.path.join(root, file)
            matches_found = find_swear_words(file_path, swear_words)
            total_matches += matches_found

    if total_matches:
        print(f'  {BOLD}{total_matches} offenders found in total.{ENDC}')

def main():
    swear_words_file = 'swear_words.txt'  # Assumes this file is in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    swear_words_path = os.path.join(script_dir, swear_words_file)
    swear_words = load_swear_words(swear_words_path)
    
    if not swear_words:
        print(f"No swear words loaded from {swear_words_file}. Please check the file.")
        return

    scan_directory('.', swear_words)

if __name__ == "__main__":
    main()
