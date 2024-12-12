import os
import re

DIR = "problems"
FILE_PATTERN = re.compile(r"\d{4}[A-Z]\d?\.py")
RUFF_LINE = "# ruff: noqa: E731, E741\n"


def main():
    already_ruffified = True
    for filename in os.listdir(DIR):
        full = os.path.join(DIR, filename)
        if not FILE_PATTERN.fullmatch(filename) or not os.path.isfile(full):
            continue
        try:
            with open(full, "r") as file:
                lines = file.readlines()
            assert lines
        except Exception as e:
            print(f"Error reading {full}: {e}")
            continue

        if lines[0] == RUFF_LINE:
            continue

        if lines[0].startswith(("# ruff", "#ruff")):
            lines[0] = RUFF_LINE
        else:
            lines.insert(0, RUFF_LINE)

        try:
            with open(full, "w") as file:
                file.writelines(lines)
            print(f"Ruffified file: {full}")
            already_ruffified = False
        except Exception as e:
            print(f"Error writing to {full}: {e}")
    if already_ruffified:
        print("All files are already ruffified!")


if __name__ == "__main__":
    main()
