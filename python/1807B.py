for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    print("YES" if sum(-n if n & 1 else n for n in a) > 0 else "NO")
