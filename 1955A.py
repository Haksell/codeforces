for _ in range(int(input())):
    n, a, b = map(int, input().split())
    print(n * a if a * 2 < b else n // 2 * b + n % 2 * a)
