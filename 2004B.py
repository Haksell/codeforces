for _ in range(int(input())):
    (la, ra) = map(int, input().split())
    (lb, rb) = map(int, input().split())
    if la > rb or lb > ra:
        print(1)
    else:
        interval = min(ra, rb) - max(la, lb)
        print(interval + (la != lb) + (ra != rb))
