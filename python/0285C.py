# ruff: noqa: E731, E741
n = int(input())
a = sorted(map(int, input().split()))
print(sum(abs(i - ai) for i, ai in enumerate(a, 1)))
