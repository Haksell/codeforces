for _ in range(int(input())):
    x, y = map(int, input().split())
    y_screens = (y + 1) >> 1
    x -= 15 * y_screens - 4 * y
    print(y_screens + max(0, (x + 14) // 15))
