# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(s):
    seen = set()
    for i in range(2, len(s) - 1):
        seen.add(s[i - 2] + s[i - 1])
        if s[i] + s[i + 1] in seen:
            return True
    return False


def main():
    for _ in rir():
        read()
        print("YES" if solve(input()) else "NO")


if __name__ == "__main__":
    main()
