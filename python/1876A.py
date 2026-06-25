# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, p = mir()
    a = lmir()
    b = lmir()
    ba = sorted(zip(b, a))
    res = p
    remaining = n - 1
    for bi, ai in ba:
        if bi >= p:
            break
        used = min(remaining, ai)
        res += used * bi
        remaining -= used
        if remaining == 0:
            break
    res += remaining * p
    return res


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
