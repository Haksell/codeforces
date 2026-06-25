# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, m, k = mir()
    a = lmir()
    q = lmir()
    if k + 1 < n:
        return [False] * m
    if k == n:
        return [True] * m
    missing = next((i + 1 for i in range(n - 1) if i + 1 != q[i]), n)
    return [ai == missing for ai in a]


def main():
    for _ in rir():
        print("".join("1" if b else "0" for b in solve()))


if __name__ == "__main__":
    main()
