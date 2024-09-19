for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(map(abs, a))
    if 0 not in a and sum(ai < 0 for ai in a) & 1:
        s -= 2 * min(map(abs, a))
    print(s)
