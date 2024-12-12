# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        x, y = mir()
        print("YES" if x >= y or x >= 4 or (x == 2 and y == 3) else "NO")


if __name__ == "__main__":
    main()
