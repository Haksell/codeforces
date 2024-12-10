# ruff: noqa: E731, E741
for _ in range(int(input())):
    res = int(input())
    a = list(map(int, input().split()))
    b = False
    last = 0
    for n in reversed(a):
        if b:
            if n > last:
                print(res)
                break
        elif n < last:
            b = True
        last = n
        res -= 1
    else:
        print(0)
