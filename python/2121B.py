# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    read()
    s = input()
    present = [False] * 26
    for c in s[:-1]:
        x = ord(c) - 97
        if present[x]:
            return True
        present[x] = True
    return s[-1] in s[1:-1]


def main():
    for _ in rir():
        print("YES" if solve() else "NO")


if __name__ == "__main__":
    main()
