# ruff: noqa: E731, E741
n = int(input())
a = list(map(int, input().split()))
last = 0
work = 0
for x in a:
    if x == 3:
        work += 1
        last = 3 if last in (0, 3) else 3 - last
    elif x == 0 or last == x:
        last = 0
    else:
        work += 1
        last = x
print(n - work)
