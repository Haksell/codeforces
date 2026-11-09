for _ in range(int(input())):
    d = input()[-1]
    s = input()
    for i, c in enumerate(s):
        if d > c:
            print(s[:i] + d + s[i:])
            break
    else:
        print(s + d)
