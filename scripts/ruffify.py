import os
import re

FILE_PATTERN = re.compile(r"\d{4}[A-Z]\d?\.py")
RUFF_LINE = "# ruff: noqa: E731, E741\n"


def main():
    for filename in os.listdir():
        if not FILE_PATTERN.fullmatch(filename) or not os.path.isfile(filename):
            continue
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
            assert lines
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            continue

        if lines[0] == RUFF_LINE:
            continue

        if lines[0].startswith(("# ruff", "#ruff")):
            lines[0] = RUFF_LINE
        else:
            lines.insert(0, RUFF_LINE)

        try:
            with open(filename, "w") as file:
                file.writelines(lines)
            print(f"Processed file: {filename}")
        except Exception as e:
            print(f"Error writing to {filename}: {e}")


if __name__ == "__main__":
    main()
