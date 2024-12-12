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
        *dims, k = mir()
        x, y, z = sorted(dims)
        r = 0
        for d1 in range(1, x + 1):
            if k % d1 != 0:
                continue
            for d2 in range(d1, y + 1):
                if k % (d1 * d2) != 0:
                    continue
                d3 = k // (d1 * d2)
                if d3 <= z:
                    r = max(r, (x - d1 + 1) * (y - d2 + 1) * (z - d3 + 1))
        print(r)


if __name__ == "__main__":
    main()
