# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, m = mir()
    regions = [[] for _ in range(m)]
    for _ in range(n):
        name, region, points = input().split()
        region = int(region)
        points = int(points)
        regions[region - 1].append((points, name))
    for region in regions:
        m1 = max(p for p, _ in region)
        best1 = [(p, n) for p, n in region if p == m1]
        if len(best1) == 1:
            m2 = max(p for p, _ in region if p != m1)
            best2 = [(p, n) for p, n in region if p == m2]
            if len(best2) == 1:
                print(best1[0][1], best2[0][1])
            else:
                print("?")
        elif len(best1) == 2:
            print(best1[0][1], best1[1][1])
        else:
            print("?")


if __name__ == "__main__":
    main()
