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
    a = lmir()
    m = max(a)
    s = sum(a)
    print("YES" if s & 1 == 0 and m <= s - m else "NO")


if __name__ == "__main__":
    main()
