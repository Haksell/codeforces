for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    print(next(i for i, n in enumerate(a, 1) if a.count(n) == 1))
