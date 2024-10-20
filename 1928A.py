for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    print("NO" if a & 1 and (b & 1 or a << 1 == b) else "YES")
