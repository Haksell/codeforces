for _ in range(int(input())):
    a, b, n, s = map(int, input().split())
    print("NO" if s > a * n + b or s % n > b else "YES")