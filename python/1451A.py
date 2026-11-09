for _ in range(int(input())):
    n = int(input())
    print(n - 1 if n <= 3 else 2 + (n & 1))
