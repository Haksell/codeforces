# ruff: noqa: E731, E741
input()
a = list(map(int, input().split()))
mini = min(a)
maxi = max(a)
print(sum(mini < ai < maxi for ai in a))
