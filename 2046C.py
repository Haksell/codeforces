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


class SegmentTree:
    def __init__(self, data):
        self.__n = len(data)
        self.__tree = [0] * (2 * self.__n)
        for i in range(self.__n):
            self.__tree[self.__n + i] = data[i]
        for i in range(self.__n - 1, 0, -1):
            self.__tree[i] = self.__tree[i << 1] + self.__tree[i << 1 | 1]

    def __len__(self):
        return self.__n

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__tree[self.__n:]})"

    def __getitem__(self, i):
        return self.__tree[i + self.__n]

    def __setitem__(self, i, value):
        i += self.__n
        self.__tree[i] = value
        while i > 1:
            i >>= 1
            self.__tree[i] = self.__tree[i << 1] + self.__tree[i << 1 | 1]

    def range_sum(self, left, right):
        left += self.__n
        right += self.__n
        res = 0
        while left < right:
            if left & 1:
                res += self.__tree[left]
                left += 1
            if right & 1:
                right -= 1
                res += self.__tree[right]
            left >>= 1
            right >>= 1
        return res


def main():
    for _ in rir():
        fuzz = random.randint(1, 1 << 30)
        points = defaultdict(list)
        for _ in rir():
            x, y = mir()
            points[x + fuzz].append(y + fuzz)

        unique_ys = sorted({y for ys in points.values() for y in ys})
        ny = len(unique_ys)
        y_map = {y: i for i, y in enumerate(unique_ys)}

        left = SegmentTree([0] * ny)
        right = SegmentTree([0] * ny)
        for ys in points.values():
            for y in ys:
                right[y_map[y]] += 1

        best_min = best_x = best_y = 0
        for x, ys in sorted(points.items()):
            lo = 1
            hi = ny - 1
            while lo <= hi:
                mi = lo + hi >> 1
                bl = left.range_sum(0, mi)
                tl = left.range_sum(mi, ny)
                br = right.range_sum(0, mi)
                tr = right.range_sum(mi, ny)
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
                left[idx] += 1
                right[idx] -= 1
        print(best_min)
        print(best_x, best_y)


if __name__ == "__main__":
    main()
