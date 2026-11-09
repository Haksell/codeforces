for _ in range(int(input())):
    n = int(input())
    print((n << 1) - bin(n).count("1"))
