for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    print(sum(a) - 2 * min(x + y for x, y in zip(a, a[1:])))