# ruff: noqa: E731, E741
n = int(input())
a = list(map(int, input().split()))
m = int(input())
ridx = {a[i]: i for i in range(n)}
left = right = 0
for q in map(int, input().split()):
    left += ridx[q] + 1
    right += n - ridx[q]
print(left, right)
