for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    print(min(max(x, y) for x, y in zip(a, a[1:])) - 1)
