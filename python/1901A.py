for _ in range(int(input())):
    n, x = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    a += [2 * x - ai for ai in reversed(a)]
    print(max((a2 - a1) for a1, a2 in zip(a, a[1:])))
