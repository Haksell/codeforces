from itertools import accumulate
from operator import xor


for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    acc = list(accumulate(a, xor, initial=0))
    for _ in range(q):
        lo, hi, k = map(int, input().split())
        print(
            "YES"
            if (acc[-1] ^ acc[lo - 1] ^ acc[hi] ^ ((hi ^ lo ^ 1) & k)) & 1
            else "NO"
        )
