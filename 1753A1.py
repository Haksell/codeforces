for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 1:
        print(-1)
    else:
        res = []
        for i in range(0, n, 2):
            if a[i] == a[i + 1]:
                res.append((i + 1, i + 2))
            else:
                res.append((i + 1, i + 1))
                res.append((i + 2, i + 2))
        print(len(res))
        for l, r in res:
            print(l, r)
