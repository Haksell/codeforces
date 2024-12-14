# ruff: noqa: E731, E741
def f(n):
    return 0 if n < 10 else 1 + f(sum(map(int, str(n))))


s = input()
if len(s) == 1:
    print(0)
else:
    n = sum(map(int, s))
    print(f(n) + 1)
