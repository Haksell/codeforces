# ruff: noqa: E731, E741
def f(x, a):
    return sum(divmod(x, a))


for _ in range(int(input())):
    l, r, a = map(int, input().split())
    res = f(r, a)
    x = r // a * a - 1
    if x >= l:
        res = max(res, f(x, a))
    print(res)
