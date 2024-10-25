def solve(n, a):
    evens = sorted(ai for ai in a if not ai & 1)
    if len(evens) == n:
        return 0
    odd = max(ai for ai in a if ai & 1)
    for e in evens:
        if e > odd:
            return len(evens) + 1
        odd += e
    return len(evens)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
