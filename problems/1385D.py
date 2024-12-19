# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def good(s, c):
    if len(s) == 1:
        return int(s[0] != c)
    a = s[: len(s) >> 1]
    b = s[len(s) >> 1 :]
    return min(
        len(a) - a.count(c) + good(b, c + 1),
        len(b) - b.count(c) + good(a, c + 1),
    )


def main():
    for _ in rir():
        read()
        s = [ord(c) - 97 for c in input()]
        print(good(s, 0))


if __name__ == "__main__":
    main()
