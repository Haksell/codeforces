for _ in range(int(input())):
    n, c, d = map(int, input().split())
    b = sorted(map(int, input().split()))
    nums = sorted(b[0] + y * c + x * d for y in range(n) for x in range(n))
    print("YES" if b == nums else "NO")
