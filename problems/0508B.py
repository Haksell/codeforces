# ruff: noqa: E731, E741
a = list(map(int, input()))
if all(n & 1 for n in a):
    print(-1)
else:
    last = a[-1]
    for i, ai in enumerate(a):
        if ai & 1 == 0:
            if ai < last:
                a[i], a[-1] = a[-1], a[i]
                break
            else:
                lasti = i
    else:
        a[lasti], a[-1] = a[-1], a[lasti]
    print("".join(map(str, a)))
