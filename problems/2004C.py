# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    if n & 1:
        print(a[0] + max(0, sum(a[2::2]) - sum(a[1::2]) - k))
    else:
        print(max(0, sum(a[1::2]) - sum(a[0::2]) - k))
