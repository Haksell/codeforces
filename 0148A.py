*l, d = (int(input()) for _ in range(5))
res = [False] * d
for x in l:
    for y in range(x - 1, d, x):
        res[y] = True
print(sum(res))