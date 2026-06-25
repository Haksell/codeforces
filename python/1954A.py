# ruff: noqa: E731, E741
def int_ceil(numer, denom):
    return (numer + denom - 1) // denom


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    print("NO" if k >= n - int_ceil(n, m) else "YES")
