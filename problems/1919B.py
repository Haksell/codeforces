# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    plus = input().count("+")
    minus = n - plus
    print(abs(plus - minus))
