# ruff: noqa: E731, E741
from statistics import mean

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if mean(a) in a else "NO")
