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
        a, b = mir()
        s = max(max(a, b), 2 * min(a, b))
        print(s**2)


if __name__ == "__main__":
    main()
