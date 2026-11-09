for _ in range(int(input())):
    n = int(input())
    s = input()
    for i in range(n >> 1):
        if s[i] == s[~i]:
            print(n - (i << 1))
            break
    else:
        print(n & 1)
