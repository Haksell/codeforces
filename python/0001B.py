# ruff: noqa: E731, E741
import re
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def standard_to_excel(col):
    col = int(col)
    digits = []
    while col > 0:
        col, d = divmod(col - 1, 26)
        digits.append(chr(65 + d))
    return "".join(reversed(digits))


def excel_to_standard(col):
    res = 0
    for d in col:
        res = 26 * res + ord(d) - 64
    return res


def main():
    for _ in rir():
        s = input()
        if re.fullmatch(r"R\d+C\d+", s):
            row, col = re.findall(r"\d+", s)
            print(f"{standard_to_excel(col)}{row}")
        else:
            col, row = re.fullmatch(r"([A-Z]+)(\d+)", s).groups()
            print(f"R{row}C{excel_to_standard(col)}")


if __name__ == "__main__":
    main()
