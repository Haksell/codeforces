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
        r = 10 ** s.count("?")
        print(0 if s[0] == "0" else r * 9 // 10 if s[0] == "?" else r)


if __name__ == "__main__":
    main()
