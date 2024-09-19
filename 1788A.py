for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c2 = a.count(2)
    if c2 & 1:
        print(-1)
    elif c2 == 0:
        print(1)
    else:
        for i, ai in enumerate(a, 1):
            if ai == 2:
                c2 -= 2
                if c2 == 0:
                    print(i)
                    break
