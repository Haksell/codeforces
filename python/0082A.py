# ruff: noqa: E731, E741
def f(n):
    return n if n < 5 else f(n - 5 >> 1)


print(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"][f(int(input()) - 1)])
