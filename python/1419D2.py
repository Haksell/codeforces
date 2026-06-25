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
    a = iter(sorted(mir()))
    res = [None] * n
    for i in range(1, n, 2):
        res[i] = next(a)
    for i in range(0, n, 2):
        res[i] = next(a)
    print(sum(res[i - 1] > res[i] < res[i + 1] for i in range(1, n - 1)))
    print(*res)


if __name__ == "__main__":
    main()
