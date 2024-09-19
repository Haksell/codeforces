for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    oa = a.count(1)
    ob = max(0, 2 * n - s)
    print("NO" if n == 1 or oa + ob > n else "YES")
