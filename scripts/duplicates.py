from collections import defaultdict
import os


def title(s):
    print(f" {s} ".center(40, "="))


def bold_cyan(text):
    return f"\033[1;36m{text}\033[0m"


def show_standalone_duplicates(standalone):
    title("STANDALONE DUPLICATES")
    for files in standalone.values():
        if len(files) >= 2:
            print(
                " == ".join(
                    bold_cyan(file) if os.path.islink(file) else file for file in files
                )
            )


def show_subtasks(subtasks):
    title("SUBTASKS")
    for k, v in sorted(subtasks.items()):
        print(k, v.keys())


def main():
    standalone = defaultdict(list)
    subtasks = defaultdict(dict)
    for file in sorted(os.listdir()):
        if not file.endswith(".py"):
            continue
        content = open(file).read()
        if file[-4].isdigit():
            subtasks[file[:-4]][file[-4]] = content
        else:
            standalone[content].append(file)
    show_standalone_duplicates(standalone)
    show_subtasks(subtasks)


if __name__ == "__main__":
    main()
