for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = min(a)
    print(sum(x != m for x in a))
