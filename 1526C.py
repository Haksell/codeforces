# TODO: part 2

from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))
acc = list(accumulate(max(ai, 0) for ai in a))
negative_idx = sorted(
    [i for i, ai in enumerate(a) if ai < 0], key=a.__getitem__, reverse=True
)
res = sum(ai >= 0 for ai in a)

for i in negative_idx:
    if all(acc[j] + a[i] >= 0 for j in range(i, n)):
        res += 1
        for j in range(i, n):
            acc[j] += a[i]
print(res)
