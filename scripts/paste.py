import os
import pyperclip
import re


def main():
    while True:
        try:
            filename = input("> ")
        except EOFError:
            print()
            return
        re_match = re.fullmatch(r"(\d{1,4})([a-zA-Z]\d?)", filename)
        assert re_match
        contest, problem = re_match.groups()
        filename = contest.zfill(4) + problem.upper() + ".py"
        if os.path.exists(filename):
            print(f"{filename} already exists")
            continue
        content = pyperclip.paste()
        if len(content) < 7:
            print("content too small")
            continue
        with open(filename, "w") as f:
            f.write(content)
        print(f"written to {filename}")


if __name__ == "__main__":
    main()
