import os
from pathlib import Path
import re
import sys

IN_DIR = "problems"
OUT_DIR = "templatized"
FILE_PATTERN = re.compile(r"\d{4}[A-Z]\d?\.py")
RUFF_LINE = "# ruff: noqa: E731, E741\n"


def read_file(filepath):
    try:
        with open(filepath) as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        sys.exit(1)


def write_file(filepath, content):
    try:
        with open(filepath, "w") as file:
            return file.write(content)
    except Exception as e:
        print(f"Error writing {filepath}: {e}")
        sys.exit(1)


def templatize(content):
    return content + "?"


def main():
    Path(OUT_DIR).mkdir(parents=True, exist_ok=True)
    already_templatized = True
    for filename in sorted(os.listdir(IN_DIR))[::100]:
        filepath = os.path.join(IN_DIR, filename)
        if not FILE_PATTERN.fullmatch(filename) or not os.path.isfile(filepath):
            continue
        content = read_file(filepath)
        templatized = templatize(content)
        if content != templatized:
            already_templatized = False
            print(f" {filename} ".center(80, "="))
            print(content, end="" if content.endswith("\n") else "\n")
            print("-" * 80)
            print(templatized, end="" if templatized.endswith("\n") else "\n")
            # write_file(os.path.join(OUT_DIR, filename), templatized)
    if already_templatized:
        print("All files are already templatized!")


if __name__ == "__main__":
    main()
