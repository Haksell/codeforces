# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        j = n - i
        print("()" * i + "(" * j + ")" * j)
