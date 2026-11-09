for _ in range(int(input())):
    n, k = map(int, input().split())
    if k & 1:
        print("NO" if n & 1 and n < k else "YES")
    else:
        print("NO" if n & 1 else "YES")
