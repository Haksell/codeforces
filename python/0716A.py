# ruff: noqa: E731, E741
_, c = map(int, input().split())
t = list(map(int, input().split()))
start = 0
ans = 0
for i, x in enumerate(t):
    if i > 0 and t[i] > t[i - 1] + c:
        start = i
    ans = i - start + 1
print(ans)
