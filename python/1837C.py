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
        s = list(input())
        last = "0"
        for i, c in enumerate(s):
            if c == "?":
                s[i] = last
            else:
                last = c
        print("".join(s))


if __name__ == "__main__":
    main()
