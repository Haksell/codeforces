def cmp(x, y):
    return (x > y) - (x < y)


for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    n1 = cmp(a, c) + cmp(b, d)
    n2 = cmp(a, d) + cmp(b, c)
    wins = (n1 > 0) + (n2 > 0)
    print(wins << 1)
