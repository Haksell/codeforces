# ruff: noqa: E731, E741
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ma = mb = 0
for ai, bi in zip(a, b):
    ma, mb = max(ma, ai + mb), max(mb, bi + ma)
print(max(ma, mb))
