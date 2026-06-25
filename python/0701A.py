# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    a = lmir()
    indices = sorted(range(n), key=a.__getitem__)
    for i in range(n >> 1):
        print(indices[i] + 1, indices[~i] + 1)


if __name__ == "__main__":
    main()
