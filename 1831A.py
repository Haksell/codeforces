for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(*[n - ai + 1 for ai in a])
