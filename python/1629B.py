# ruff: noqa: E731, E741
for _ in range(int(input())):
    l, r, k = map(int, input().split())
    if l == r:
        print("NO" if l == 1 else "YES")
    else:
        odds = (r - l + 1 >> 1) + (l & r & 1)
        print("YES" if k >= odds else "NO")
