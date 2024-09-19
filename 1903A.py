for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print("NO" if k == 1 and any(y < x for x, y in zip(a, a[1:])) else "YES")
