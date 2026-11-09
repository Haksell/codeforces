for _ in range(int(input())):
    _, k = map(int, input().split())
    print("YES" if k in map(int, input().split()) else "NO")
