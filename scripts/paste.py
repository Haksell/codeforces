import re
import sys

import pyperclip


def main():
    assert len(sys.argv) == 2
    filename = sys.argv[1]
    re_match = re.fullmatch(r"(\d{1,4})([a-zA-Z]\d?)", filename)
    assert re_match
    contest, problem = re_match.groups()
    filename = contest.zfill(4) + problem.upper() + ".py"
    content = pyperclip.paste()
    open(filename, "w").write(content)
    print(f"Written to {filename}")


if __name__ == "__main__":
    main()
