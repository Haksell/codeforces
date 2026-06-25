# ruff: noqa: E731, E741
from string import ascii_lowercase

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = ascii_lowercase[:b]
    print("".join(s[i % b] for i in range(n)))
