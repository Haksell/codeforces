for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))[::-1]
    b = list(map(int, input().split()))
    res = 0
    for bi in b:
        if a[-1] <= bi:
            a.pop()
        else:
            res += 1
    print(res)
