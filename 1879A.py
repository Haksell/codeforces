for _ in range(int(input())):
    n = int(input())
    ps, pe = map(int, input().split())
    others = [list(map(int, input().split())) for _ in range(n - 1)]
    print(ps if all(s < ps or e < pe for s, e in others) else -1)
