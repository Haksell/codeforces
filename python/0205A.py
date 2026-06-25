# ruff: noqa: E731, E741
n = int(input())
a = list(map(int, input().split()))
mini = min(a)
print("Still Rozdil" if a.count(mini) >= 2 else a.index(mini) + 1)
