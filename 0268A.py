from collections import defaultdict

d1 = defaultdict(int)
d2 = defaultdict(int)
for _ in range(int(input())):
    n1, n2 = map(int, input().split())
    d1[n1] += 1
    d2[n2] += 1

print(sum(d1[n] * d2[n] for n in d2))
