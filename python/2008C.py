import math


def inverse_triangle(n):
    return math.floor((2 * n + 0.25) ** 0.5 + 0.5)


for _ in range(int(input())):
    lo, hi = map(int, input().split())
    print(inverse_triangle(hi - lo))
