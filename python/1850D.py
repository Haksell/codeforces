# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    prev = a[0]
    best = curr = 1
    for x in a[1:]:
        curr = 1 if x - k > prev else curr + 1
        best = max(best, curr)
        prev = x
    print(n - best)
