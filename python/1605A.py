for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(min(1, (a + b + c) % 3))
