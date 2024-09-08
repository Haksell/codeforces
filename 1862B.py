for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    res = [b[0]]
    for bi in b[1:]:
        if bi < res[-1]:
            res.append(1)
        res.append(bi)
    print(len(res))
    print(*res)
