# ruff: noqa: E731, E741
from collections import defaultdict
import random
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


class FenwickTree:
    def __init__(self, size):
        self.__len = size
        self.__tree = [0] * (size + 1)

    def update(self, i, delta):
        i += 1
        while i <= self.__len:
            self.__tree[i] += delta
            i += i & -i

    def prefix_sum(self, i):
        res = 0
        while i > 0:
            res += self.__tree[i]
            i -= i & -i
        return res


def main():
    for _ in rir():
        fuzz = random.randint(1, 1 << 30)
        num_points = ir()
        points = defaultdict(list)
        for _ in range(num_points):
            x, y = mir()
            points[x + fuzz].append(y + fuzz)

        unique_ys = sorted({y for ys in points.values() for y in ys})
        ny = len(unique_ys)
        y_map = {y: i for i, y in enumerate(unique_ys)}

        left = FenwickTree(ny)
        right = FenwickTree(ny)
        for ys in points.values():
            for y in ys:
                right.update(y_map[y], 1)

        best_min = best_x = best_y = left_total = 0
        for x, ys in sorted(points.items()):
            lo = 1
            hi = ny - 1
            while lo <= hi:
                mi = lo + hi >> 1
                bl = left.prefix_sum(mi)
                br = right.prefix_sum(mi)
                tl = left_total - bl
                tr = num_points - left_total - br
                m = min(bl, tl, br, tr)
                if m > best_min:
                    best_min = m
                    best_x = x - fuzz
                    best_y = unique_ys[mi] - fuzz
                if min(bl, br) < min(tl, tr):
                    lo = mi + 1
                else:
                    hi = mi - 1
            for y in ys:
                idx = y_map[y]
                left_total += 1
                left.update(idx, 1)
                right.update(idx, -1)
        print(best_min)
        print(best_x, best_y)


if __name__ == "__main__":
    main()
