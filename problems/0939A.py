# ruff: noqa: E731, E741
n = int(input())
p = [int(x) - 1 for x in input().split()]
for i in range(n):
    if p[p[p[i]]] == i:
        print("YES")
        break
else:
    print("NO")
