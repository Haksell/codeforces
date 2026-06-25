# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c = [int(x) - 1 for x in input().split()]
    if a <= b:
        print(10**a, 10**b + 10**c)
    elif a > b:
        print(10**a + 10**c, 10**b)
