# ruff: noqa: E731, E741
def solve(n, k, x):
    if x != 1:
        return [1] * n
    if k == 1:
        return None
    if n & 1 == 0:
        return [2] * (n >> 1)
    if k == 2:
        return None
    return [3] + [2] * (n - 3 >> 1)


for _ in range(int(input())):
    n, k, x = map(int, input().split())
    res = solve(n, k, x)
    if res is None:
        print("NO")
    else:
        print("YES")
        print(len(res))
        print(*res)
