# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        read()
        a = lmir()
        print("YES" if all(abs(x - y) in (5, 7) for x, y in zip(a, a[1:])) else "NO")


if __name__ == "__main__":
    main()
