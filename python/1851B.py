for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    s = sorted(a)
    print("YES" if all((ai ^ si) & 1 == 0 for ai, si in zip(a, s)) else "NO")
