# ruff: noqa: E731, E741
def f(s):
    if s == "M":
        return 0
    abs = len(s)
    sign = -1 if s[-1] == "S" else 1
    return abs * sign


for _ in range(int(input())):
    a, b = map(f, input().split())
    print("<" if a < b else ">" if a > b else "=")
