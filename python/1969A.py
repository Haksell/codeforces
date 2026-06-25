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
        n = ir()
        p = [pi - 1 for pi in mir()]
        print(2 if any(i == p[p[i]] for i in range(n)) else 3)


if __name__ == "__main__":
    main()
