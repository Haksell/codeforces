for _ in range(int(input())):
    n = int(input())
    s = input()
    f = input()
    x = sum(si > fi for si, fi in zip(s, f))
    y = sum(si < fi for si, fi in zip(s, f))
    print(max(x, y))
