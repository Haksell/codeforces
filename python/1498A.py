# ruff: noqa: E731, E741
from itertools import count
from math import gcd

for _ in range(int(input())):
    for n in count(int(input())):
        if gcd(n, sum(map(int, str(n)))) > 1:
            print(n)
            break
