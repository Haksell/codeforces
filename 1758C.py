# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def naive(n, x):
    if n == 1:
        return [1]
    if n % x or x == 1:
        return [-1]

    def helper(arr):
        nonlocal ans
        if ans is not None:
            return
        elif len(arr) == n - 1:
            ans = arr + [1]
        else:
            d = len(arr) + 1
            for i in range(d, n + 1, d):
                if i not in arr:
                    arr.append(i)
                    helper(arr)
                    arr.pop()

    ans = None
    helper([x])
    return -1 if ans is None else ans


def factors(n):
    d = 2
    ans = []
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans


def smart(n, x):
    if n == 1:
        return [1]
    if n % x or x == 1:
        return [-1]
    ans = list(range(1, n + 1))
    ans[0] = x
    ans[x - 1] = n
    ans[-1] = 1
    last = x - 1
    for i in range(x, n - 1):
        if n % ans[i] == 0 and ans[i] % (last + 1) == 0:
            ans[i], ans[last] = ans[last], ans[i]
            last = i
    return ans


# for n in range(1, 31):
#     for x in range(1, n + 1):
#         r1 = naive(n, x)
#         r2 = smart(n, x)
#         print(n, x, naive(n, x))
#         assert r1 == r2, (n, x, r1, r2)
#     print()

for _ in rir():
    n, x = mir()
    print(*smart(n, x))
