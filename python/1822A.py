for _ in range(int(input())):
    _, t = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    valid = [i for i, ai in enumerate(a) if ai + i <= t]
    print(max(valid, key=b.__getitem__) + 1 if valid else -1)
