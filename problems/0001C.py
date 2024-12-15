# ruff: noqa: E731, E741
from math import atan2, cos, hypot, sin, tau
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def get_circumcenter(x1, y1, x2, y2, x3, y3):
    assert not (y1 == y2 == y3) and not (x1 == x2 == x3)
    if y1 == y2:
        return get_circumcenter(x1, y1, x3, y3, x2, y2)
    if y3 == y2:
        return get_circumcenter(x2, y2, x1, y1, x3, y3)
    x4 = (x1 + x2) / 2
    x5 = (x3 + x2) / 2
    y4 = (y1 + y2) / 2
    y5 = (y3 + y2) / 2
    p4 = (x1 - x2) / (y2 - y1)
    p5 = (x3 - x2) / (y2 - y3)
    x = (y5 - y4 + p4 * x4 - p5 * x5) / (p4 - p5)
    return (x, y4 + p4 * (x - x4))


def get_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * y2 - x2 * y1 + x2 * y3 - x3 * y2 + x3 * y1 - x1 * y3) / 2


def get_polygon_area(cx, cy, x1, y1, sides):
    radius = hypot(cy - y1, cx - x1)
    angle = atan2(y1 - cy, x1 - cx) + tau / sides
    x2 = cx + cos(angle) * radius
    y2 = cy + sin(angle) * radius
    return get_triangle_area(x1, y1, cx, cy, x2, y2) * sides


def divisor_float_test(numer, denom):
    x = numer / denom % 1
    return min(x, 1 - x)


def get_sides(*angle_differences):
    def test_sides(sides):
        angle = tau / sides
        return max(divisor_float_test(ad, angle) for ad in angle_differences) * sides

    return min(range(3, 101), key=test_sides)


def main():
    x1, y1, x2, y2, x3, y3 = map(float, open(0).read().split())
    cx, cy = get_circumcenter(x1, y1, x2, y2, x3, y3)
    a1 = atan2(y1 - cy, x1 - cx)
    a2 = atan2(y2 - cy, x2 - cx)
    a3 = atan2(y3 - cy, x3 - cx)
    sides = get_sides(abs(a1 - a2), abs(a2 - a3), abs(a3 - a1))
    print(get_polygon_area(cx, cy, x1, y1, sides))


if __name__ == "__main__":
    main()
