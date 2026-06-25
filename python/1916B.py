# ruff: noqa: E731, E741
import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    lcm = math.lcm(a, b)
    print(b * (b // a) if lcm == b else lcm)
