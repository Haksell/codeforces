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
        a = lmir()
        res = [-1] * n
        for i, j in enumerate(sorted(range(n), key=a.__getitem__, reverse=True)):
            res[j] = i + 1
        print(*res)


if __name__ == "__main__":
    main()
