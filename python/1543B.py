for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = sum(a) % n
    print(m * (n - m))
