# ruff: noqa: E731, E741
from string import ascii_lowercase


for _ in range(int(input())):
    n, k = map(int, input().split())
    print(n * ascii_lowercase[:k])
