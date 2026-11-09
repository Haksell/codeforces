for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    for _ in range(5):
        a += 1
        if a > c:
            a, b, c = b, c, a
        elif a > b:
            a, b = b, a
    print(a * b * c)
