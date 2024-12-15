# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n = ir()
    a = list(input())
    b = list(input())

    for i in range(n):
        a_left = i == 0 or a[i - 1] == "#"
        a_right = i == n - 1 or a[i + 1] == "#"
        b_left = i == 0 or b[i - 1] == "#"
        b_right = i == n - 1 or b[i + 1] == "#"
        if (
            a[i] == "."
            and b[i] == "."
            and ((a_left and a_right) or (b_left and b_right))
        ):
            a[i] = b[i] = "#"

    multiple = False
    for i in range(n):
        if i < n - 1 and a[i] == b[i] == a[i + 1] == b[i + 1] == ".":
            multiple = True
        elif a[i] == b[i]:
            a[i] = b[i] = "#"
        elif i == n - 1:
            return "None"
        elif a[i] == ".":
            if a[i + 1] == "#":
                return "None"
            a[i] = a[i + 1] = "#"
        elif b[i] == ".":
            if b[i + 1] == "#":
                return "None"
            b[i] = b[i + 1] = "#"

    return "Multiple" if multiple else "Unique"


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
