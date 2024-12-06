for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(min(range(n), key=a.__getitem__) + 1, max(range(n), key=a.__getitem__) + 1)