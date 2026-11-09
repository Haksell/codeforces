a = [int(input()) for _ in range(4)]
d = int(input())
res = [False] * d
for x in a:
    for y in range(x - 1, d, x):
        res[y] = True
print(sum(res))
