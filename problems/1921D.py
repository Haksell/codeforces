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
        n, _ = mir()
        a = sorted(mir())
        b = sorted(mir())
        res = 0
        above_idx = 0
        below_idx = 0
        for _ in range(n):
            above = b[~above_idx] - a[above_idx]
            below = a[~below_idx] - b[below_idx]
            if above > below:
                res += above
                above_idx += 1
            else:
                res += below
                below_idx += 1
        print(res)


if __name__ == "__main__":
    main()
