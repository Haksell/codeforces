# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    q, r = divmod(n, 3)
    print("abc" * q + "ab"[:r])
