# ruff: noqa: E731, E741
from itertools import product
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        a, b = mir()
        xk, yk = mir()
        xq, yq = mir()
        jumps = [
            (a, b),
            (a, -b),
            (-a, b),
            (-a, -b),
            (b, a),
            (b, -a),
            (-b, a),
            (-b, -a),
        ]
        print(
            len(
                {
                    (dx1, dx2, dy1, dy2)
                    for (dx1, dy1), (dx2, dy2) in product(jumps, repeat=2)
                    if xk + dx1 + dx2 == xq and yk + dy1 + dy2 == yq
                }
            )
        )


if __name__ == "__main__":
    main()
