for _ in range(int(input())):
    n = int(input())
    print(15 if n <= 6 else ((n + 1) >> 1) * 5)
