from collections import defaultdict
import os


def main():
    contents = defaultdict(list)
    for file in sorted(os.listdir()):
        if not file.endswith(".py"):
            continue
        content = open(file).read()
        contents[content].append(file)
    for v in contents.values():
        if len(v) >= 2:
            print(" == ".join(v))


if __name__ == "__main__":
    main()
