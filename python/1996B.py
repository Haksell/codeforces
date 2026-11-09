for _ in range(int(input())):
    n, k = map(int, input().split())
    for i in range(n):
        s = input()
        if i % k == 0:
            print(s[::k])
