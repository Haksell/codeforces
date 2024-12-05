# ruff: noqa: E731, E741
def solve(a):
    prev = 99
    for ai in reversed(a):
        if ai <= prev:
            prev = ai
        else:
            if ai < 10:
                return False
            t, u = divmod(ai, 10)
            if t > u or u > prev:
                return False
            prev = t
    return True


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if solve(a) else "NO")
