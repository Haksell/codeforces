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
        _, m = mir()
        a = lmir()
        d = [0] * m
        for ai in a:
            d[ai % m] += 1
        r = 0
        r += d[0] > 0
        r += m & 1 == 0 and d[m >> 1] > 0
        for i in range(1, m + 1 >> 1):
            x = d[i]
            y = d[m - i]
            if x or y:
                r += 1 + max(0, max(x, y) - min(x, y) - 1)
        print(r)


if __name__ == "__main__":
    main()
