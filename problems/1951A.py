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
        read()
        s = input()
        n = s.count("1")
        if n == 2:
            print("NO" if s.index("1") + 1 == s.rindex("1") else "YES")
        else:
            print("NO" if n & 1 else "YES")


if __name__ == "__main__":
    main()
