# ruff: noqa: E731, E741
def solve(a, k):
    if k == 1:
        return True
    first, *a, last = a
    if first == last:
        return a.count(first) >= k - 2
    target = first
    remaining = k - 1
    for ai in a:
        if ai != target:
            continue
        remaining -= 1
        if remaining == 0:
            if target == last:
                return True
            target = last
            remaining = k - 1
    return False


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print("YES" if solve(a, k) else "NO")
