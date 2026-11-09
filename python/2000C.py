def matches(x, y):
    d = dict()
    for xi, yi in zip(x, y):
        if xi not in d:
            d[xi] = yi
        elif d[xi] != yi:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for _ in range(int(input())):
        s = input()
        print("YES" if len(s) == n and matches(s, a) and matches(a, s) else "NO")
