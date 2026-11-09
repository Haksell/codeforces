for _ in range(int(input())):
    s = input()
    c = input()
    print("YES" if c in s[::2] else "NO")
