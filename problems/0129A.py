# ruff: noqa: E731, E741
n = int(input())
o = sum(ord(x[-1]) & 1 for x in input().split())
print(o if o & 1 else n - o)
