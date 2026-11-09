for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(*sorted(a, key=lambda n: n & 1))
