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
        ia = s.find("a", 1)
        if ia != -1 and ia != len(s) - 1:
            print(s[:ia], "a", s[ia + 1 :])
        else:
            print(s[0], s[1:-1], s[-1])


if __name__ == "__main__":
    main()
