# ruff: noqa: E731, E741
n = int(input())
a = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    wire, left = [int(x) - 1 for x in input().split()]
    right = a[wire] - left - 1
    a[wire] = 0
    if wire != 0:
        a[wire - 1] += left
    if wire != n - 1:
        a[wire + 1] += right
print(*a, sep="\n")
