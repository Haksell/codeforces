# ruff: noqa: E731, E741
_, k, x = map(int, input().split())
a = sorted(map(int, input().split()))
diffs = sorted([r - l for l, r in zip(a, a[1:]) if r - l > x], reverse=True)
while diffs:
    needed = (diffs[-1] - 1) // x
    if needed > k:
        break
    k -= needed
    diffs.pop()
print(len(diffs) + 1)
