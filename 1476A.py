# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    if k >= n:
        print(-(-k // n))
    else:
        print(1 if n % k == 0 else 2)
