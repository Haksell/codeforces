for _ in range(int(input())):
    a = list(map(int, input().split()))
    i = sorted(range(4), key=a.__getitem__)
    print("NO" if sum(i[-2:]) in [1, 5] else "YES")
