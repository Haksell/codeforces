for _ in range(int(input())):
    a, b, _ = map(int, input().split())
    x = list(map(int, input().split()))
    print(sum(min(xi, a - 1) for xi in x) + b)
