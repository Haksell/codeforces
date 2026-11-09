for _ in range(int(input())):
    b, c, h = map(int, input().split())
    print(2 * min(b - 1, c + h) + 1)
