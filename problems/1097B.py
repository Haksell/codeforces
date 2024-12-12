# ruff: noqa: E731, E741
n = int(input())
a = [int(input()) for _ in range(n)]
for i in range(1 << n):
    b = [n if 1 << j & i else -n for j, n in enumerate(a)]
    if sum(b) % 360 == 0:
        print("YES")
        break
else:
    print("NO")
