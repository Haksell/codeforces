# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        s = input()
        print(1 if any(a == b for a, b in zip(s, s[1:])) else len(s))


if __name__ == "__main__":
    main()
