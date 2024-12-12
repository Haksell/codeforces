import os
import pyperclip
import re
import readline  # noqa: F401

DIR = "problems"


def main():
    while True:
        try:
            filename = input("> ")
        except EOFError:
            print()
            break

        re_match = re.fullmatch(r"(\d{1,4})([a-zA-Z]\d?)", filename)
        if not re_match:
            print("Invalid problem.")
            continue

        contest, problem = re_match.groups()
        filename = os.path.join(DIR, contest.zfill(4) + problem.upper() + ".py")

        if os.path.exists(filename):
            print(f"{filename} already exists")
            continue

        content = pyperclip.paste()
        if len(content) < 7:
            print("Content too small")
            continue

        with open(filename, "w") as f:
            f.write(content)
        print(f"Written to {filename}")


if __name__ == "__main__":
    main()
