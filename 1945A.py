for _ in range(int(input())):
    i, e, u = map(int, input().split())
    eq, ed = divmod(e, 3)
    print(-1 if ed and ed + u < 3 else i + eq + (ed + u + 2) // 3)
