# ruff: noqa: E731, E741
n = int(input())
a = iter(sorted(map(int, input().split())))
ans = [None] * n
for i in range(1, n, 2):
    ans[i] = next(a)
for i in range(0, n, 2):
    ans[i] = next(a)
print(~-n >> 1)
print(*ans)
