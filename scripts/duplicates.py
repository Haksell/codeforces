from collections import defaultdict
import os


DIR = "problems"


def title(s):
    print(f" {s} ".center(40, "="))


def bold_cyan(text):
    return f"\033[1;36m{text}\033[0m"


def show_files(files):
    print(
        " == ".join(
            bold_cyan(f) if os.path.islink(os.path.join(DIR, f)) else f for f in files
        )
    )


def show_standalone_duplicates(standalone):
    title("STANDALONE DUPLICATES")
    for files in standalone.values():
        if len(files) >= 2:
            show_files(files)


# TODO: handle >2 subtasks (YAGNI though)
def show_subtasks(subtasks):
    DIFFERENT = {"1243B", "2039C"}
    title("SAME SUBTASKS")
    for k, v in sorted(subtasks.items()):
        if k not in DIFFERENT:
            show_files(v)
    title("DIFFERENT SUBTASKS")
    for k, v in sorted(subtasks.items()):
        if k in DIFFERENT:
            show_files(v)


def main():
    standalone = defaultdict(list)
    subtasks = defaultdict(list)
    for file in sorted(os.listdir(DIR)):
        if not file.endswith(".py"):
            continue
        if file[-4].isdigit():
            subtasks[file[:-4]].append(file)
        else:
            content = open(os.path.join(DIR, file)).read()
            standalone[content].append(file)
    show_standalone_duplicates(standalone)
    show_subtasks(subtasks)


if __name__ == "__main__":
    main()
