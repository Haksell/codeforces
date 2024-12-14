# ruff: noqa: E731, E741
n, m = map(int, input().split())
a = list(map(int, input().split()))

res = []
s = set()
for x in reversed(a):
    if x not in s:
        s.add(x)
    res.append(len(s))
res.reverse()

for _ in range(m):
    print(res[int(input()) - 1])
