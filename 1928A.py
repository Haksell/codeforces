for _ in range(int(input())):
    a, b = map(int, input().split())
    print("No" if a & b & 1 or a == b << 1 or a << a == b else "Yes")
