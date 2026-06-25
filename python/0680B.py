# ruff: noqa: E731, E741
n, a = map(int, input().split())
a -= 1
t = [x == "1" for x in input().split()]
ans = t[a]
for i in range(1, max(a + 1, n - a + 1)):
    bools = []
    if a >= i:
        bools.append(t[a - i])
    if a + i < n:
        bools.append(t[a + i])
    ans += len(bools) * all(bools)
print(ans)
