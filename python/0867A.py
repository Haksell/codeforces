# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    read()
    s = input()
    print("YES" if s[0] == "S" and s[-1] == "F" else "NO")


if __name__ == "__main__":
    main()
