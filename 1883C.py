# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k == 4:
        cnt = [0] * 4
        for ai in a:
            cnt[ai & 3] += 1
        if cnt[0] >= 1 or cnt[2] >= 2:
            print(0)
        elif cnt[3] >= 1 or cnt[2] >= 1:
            print(1)
        else:
            print(2)
    else:
        print(min(-ai % k for ai in a))
