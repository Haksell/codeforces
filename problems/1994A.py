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
        h, w = mir()
        if h == w == 1:
            read()
            print(-1)
        elif w == 1:
            x = input()
            for _ in range(h - 1):
                print(input())
            print(x)
        else:
            for _ in range(h):
                s = input()
                i = s.index(" ")
                print(s[i + 1 :], s[:i])


if __name__ == "__main__":
    main()
