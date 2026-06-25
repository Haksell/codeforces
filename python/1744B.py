# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    on = sum(ai & 1 for ai in a)
    en = n - on
    es = sum(ai for ai in a if ai & 1 == 0)
    os = sum(ai for ai in a if ai & 1 == 1)
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 0:
            if x & 1 == 0:
                es += x * en
            else:
                os += es + x * en
                en = es = 0
                on = n
        else:
            if x & 1 == 0:
                os += x * on
            else:
                es += os + x * on
                on = os = 0
                en = n
        print(es + os)
