for _ in range(int(input())):
    n = int(input())
    d = 3
    while n % d != 0:
        d = 2 * d + 1
    print(n // d)
