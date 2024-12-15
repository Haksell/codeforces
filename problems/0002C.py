# ruff: noqa: E731, E741
from itertools import product
from math import hypot
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def weighted_barycenter(zs, rs):
    return sum(z / r for z, r in zip(zs, rs)) / sum(1 / r for r in rs)


def loss(x, y, xs, ys, rs):
    weighted_distances = [hypot(xi - x, yi - y) / ri for xi, yi, ri in zip(xs, ys, rs)]
    return max(weighted_distances) - min(weighted_distances)


def main():
    nums = list(map(int, open(0).read().split()))
    xs, ys, rs = nums[0::3], nums[1::3], nums[2::3]
    x, y = weighted_barycenter(xs, rs), weighted_barycenter(ys, rs)
    step_size = 1
    while step_size > 1e-9:
        next_x, next_y = min(
            [
                (x + dx * step_size, y + dy * step_size)
                for dx, dy in product([-1, 0, 1], repeat=2)
            ],
            key=lambda t: loss(*t, xs, ys, rs),
        )
        if next_x == x and next_y == y:
            step_size /= 2
        x, y = next_x, next_y
    if loss(x, y, xs, ys, rs) < 1e-6:
        print(f"{x:.5f} {y:.5f}")


if __name__ == "__main__":
    main()
