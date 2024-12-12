# ruff: noqa: E731, E741
k = int(input().split()[-1])
a = list(map(int, input().split()))
d = {n: i for i, n in enumerate(a, 1)}
if len(d) >= k:
    print("YES")
    print(*list(d.values())[:k])
else:
    print("NO")
