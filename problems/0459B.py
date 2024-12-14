# ruff: noqa: E731, E741
n = int(input())
b = list(map(int, input().split()))
maxi = max(b)
mini = min(b)
if maxi != mini:
    print(maxi - mini, b.count(maxi) * b.count(mini))
else:
    print(0, n * (n - 1) // 2)
