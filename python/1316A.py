for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(min(m, sum(a)))
