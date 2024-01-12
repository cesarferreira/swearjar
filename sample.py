import time
import random
from yaspin import yaspin

with yaspin() as sp:
    # Support all basic termcolor text colors
    colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    # List of fake folder names
    folders = ["Folder1", "Folder2", "Folder3", "Folder4", "Folder5"]

    for folder in folders:
        color = random.choice(colors)
        sp.color, sp.text = color, folder
        time.sleep(1)