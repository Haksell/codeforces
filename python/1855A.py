for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    print(sum(pi == i for i, pi in enumerate(p, 1)) + 1 >> 1)
