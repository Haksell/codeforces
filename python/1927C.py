# ruff: noqa: E731, E741
def solve(a, b, k):
    ka = kb = k >> 1
    for i in range(1, k + 1):
        if a[i] and b[i]:
            continue
        elif a[i]:
            ka -= 1
            if ka < 0:
                return False
        elif b[i]:
            kb -= 1
            if kb < 0:
                return False
        else:
            return False
    return True


def present(a, k):
    inside = [False] * (k + 1)
    for ai in a:
        if ai <= k:
            inside[ai] = True
    return inside


for _ in range(int(input())):
    _, _, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("YES" if solve(present(a, k), present(b, k), k) else "NO")
