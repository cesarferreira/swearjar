import os
import re

def load_swear_words(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_swear_words(file_path, swear_words):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, 1):
        for swear_word in swear_words:
            if swear_word in line:
                highlighted_line = line.replace(swear_word, f'\033[1m{swear_word}\033[0m')
                print(f'{file_path}:{line_number}: {highlighted_line.strip()}')

def scan_directory(directory, swear_words):
    for root, _, files in os.walk(directory):
        for file in files:
            # if not file.endswith('.py'):  # Skip non-Python files
            #     continue
            find_swear_words(os.path.join(root, file), swear_words)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    swear_words_file = os.path.join(script_dir, 'swear_words.txt')
    
    swear_words = load_swear_words(swear_words_file)
    scan_directory('.', swear_words)

if __name__ == "__main__":
    main()
