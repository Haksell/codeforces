import re
import sys


def main():
    assert len(sys.argv) == 2
    filename = sys.argv[1]
    content = open(filename).read()
    top = []
    bottom = []
    for x in re.split(r"(\buse\b[^;]*;)", content):
        if x.startswith("use "):
            top.append(x + "\n\n")
        else:
            bottom.append(x)
    open(filename, "w").write("".join(top + bottom))


if __name__ == "__main__":
    main()
