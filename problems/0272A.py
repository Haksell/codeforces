# ruff: noqa: E731, E741
n = int(input())
t = sum(map(int, input().split()))
print(sum((t + i) % (n + 1) != 1 for i in range(1, 6)))
