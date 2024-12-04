from collections import defaultdict
import os


def bold_cyan(text):
    return f"\033[1;36m{text}\033[0m"


def main():
    contents = defaultdict(list)
    for file in sorted(os.listdir()):
        if not file.endswith(".py"):
            continue
        content = open(file).read()
        contents[content].append(file)
    for files in contents.values():
        if len(files) >= 2:
            print(
                " == ".join(
                    bold_cyan(file) if os.path.islink(file) else file for file in files
                )
            )


if __name__ == "__main__":
    main()
