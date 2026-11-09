for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if a + b + c - min(a, b, c) >= 10 else "NO")
