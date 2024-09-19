for _ in range(int(input())):
    n, m = map(int, input().split())
    print("Yes" if n & 1 == m & 1 and n >= m else "No")
