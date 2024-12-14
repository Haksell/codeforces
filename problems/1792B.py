# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(a1, a2, a3, a4):
    if a1 == 0:
        return 0 if a2 == a3 == a4 == 0 else 1
    x = min(a2, a3)
    y = max(a2, a3) - x
    m = a1
    res = a1 + 2 * x
    if y > m:
        return res + m + 1
    m -= y
    res += y
    return res + min(m + 1, a4)


def main():
    for _ in rir():
        a1, a2, a3, a4 = mir()
        print(solve(a1, a2, a3, a4))


if __name__ == "__main__":
    main()
