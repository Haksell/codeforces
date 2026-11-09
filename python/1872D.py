import math


def sum_range(start, end):
    return (start + end) * (end - start + 1) >> 1


for _ in range(int(input())):
    n, x, y = map(int, input().split())
    lcm_xy = math.lcm(x, y)
    lcm_count = n // lcm_xy
    x_count = n // x - lcm_count
    y_count = n // y - lcm_count
    print(sum_range(n - x_count + 1, n) - sum_range(1, y_count))
