import pyperclip
import re
import readline  # noqa: F401


def read_input():
    problem = input("Problem ID: ")
    re_match = re.fullmatch(r"(\d{1,4})([a-zA-Z]\d?)", problem)
    assert re_match
    contest, problem = re_match.groups()
    problem = contest.zfill(4) + problem.upper()

    stdin = input("Enter when clipboard contains stdin: ")
    assert not stdin
    stdin = pyperclip.paste()

    stdout = input("Enter when clipboard contains stdout: ")
    assert not stdout
    stdout = pyperclip.paste()

    return problem, stdin, stdout


def main():
    while True:
        try:
            problem, stdin, stdout = read_input()
        except EOFError:
            break

        new_test = f"""\
        (
            "{problem}",
            "\\
{stdin}",
            "\\
{stdout}",
        ),"""
        lines = open("tests/test_all.rs").read().strip().split("\n")
        lines.insert(-2, new_test)
        print("\n".join(lines), file=open("tests/test_all.rs", "w"))
        print(f"Test {problem} added.")


if __name__ == "__main__":
    main()
