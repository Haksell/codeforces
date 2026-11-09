for _ in range(int(input())):
    xc, yc, k = map(int, input().split())
    if k & 1:
        print(xc, yc)
    for i in range(1, (k >> 1) + 1):
        print(xc + i, yc)
        print(xc - i, yc)
