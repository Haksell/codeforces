# ruff: noqa: E731, E741
for _ in range(int(input())):
    x = int(input())
    l = list(map(int, input().split()))
    print("NO" if l[x - 1] == 0 or l[l[x - 1] - 1] == 0 else "YES")
