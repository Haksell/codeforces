# ruff: noqa: E731, E741
def solve(v, c, t1, t2):
    if n + m > v + c:
        return False
    return t2 <= t1 - abs(c - v) or t2 <= min(c, v)


for _ in range(int((input()))):
    v, c, n, m = map(int, input().split())
    print("YES" if solve(v, c, n, m) else "NO")
