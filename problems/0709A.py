# ruff: noqa: E731, E741
n, b, d = map(int, input().split())
a = map(int, input().split())
res = x = 0
for o in a:
    if o <= b:
        x += o
        if x > d:
            res += 1
            x = 0
print(res)
