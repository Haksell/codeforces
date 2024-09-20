from functools import reduce
from operator import xor


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = reduce(xor, a)
    print(x if n & 1 or x == 0 else -1)
