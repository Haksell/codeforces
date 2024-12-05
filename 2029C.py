# ruff: noqa: E731, E741
def valid(a, first_occ, target):
    for i, ai in reversed(list(enumerate(a, 1))):
        target += 1 if ai < target else -1
        if target < len(first_occ) and first_occ[target] < i:
            return True
    return False


def solve(n, a):
    if all(ai > i for i, ai in enumerate(a)):
        return n - 1
    first_occ = [0]
    acc = 0
    for i, ai in enumerate(a, 1):
        acc += (ai > acc) - (ai < acc)
        if acc == len(first_occ):
            first_occ.append(i)
    lo = len(first_occ) - 1
    hi = n - 1
    while lo < hi:
        mi = (lo + hi + 1) >> 1
        if valid(a, first_occ, mi):
            lo = mi
        else:
            hi = mi - 1
    return lo


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
