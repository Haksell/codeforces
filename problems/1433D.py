# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if all(ai == a[0] for ai in a):
        print("NO")
    else:
        print("YES")
        snd = next(i + 1 for i in range(n) if a[i] != a[0])
        print(1, snd)
        for i, ai in enumerate(a, 1):
            if i == 1 or i == snd:
                continue
            elif ai == a[0]:
                print(snd, i)
            else:
                print(1, i)
