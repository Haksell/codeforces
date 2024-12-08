# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = input()
    print(sum(map(int, s)) + sum(c != "0" for c in s[:-1]))
