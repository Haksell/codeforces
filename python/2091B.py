# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    _, x = mir()
    a = sorted(mir(), reverse=True)
    res = cur = m = 0
    for ai in a:
        m = ai
        cur += 1
        if cur * m >= x:
            res += 1
            cur = 0
    print(res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
