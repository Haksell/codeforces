# ruff: noqa: E731, E741
input()
a = list(map(int, input().split()))
d = sum(1 if n == 0 else n - 1 if n >= 1 else -1 - n for n in a)
print(d + 2 if 0 not in a and sum(n < 0 for n in a) & 1 else d)
