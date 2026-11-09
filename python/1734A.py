for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    print(min(z - x for x, z in zip(a, a[2:])))
