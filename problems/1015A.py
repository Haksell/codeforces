# ruff: noqa: E731, E741
n, m = map(int, input().split())
ans = set(range(1, m + 1))
for _ in range(n):
    l, r = map(int, input().split())
    ans -= set(range(l, r + 1))
print(len(ans))
print(*ans)
