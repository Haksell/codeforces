for _ in range(int(input())):
    h, w = map(int, input().split())
    print(h * (w >> 1))
