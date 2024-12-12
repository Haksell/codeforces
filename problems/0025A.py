# ruff: noqa: E731, E741
input()
a = list(map(int, input().split()))
o = sum(n & 1 for n in a)
goal = o == 1
print(next(i + 1 for i, n in enumerate(a) if n & 1 == goal))
