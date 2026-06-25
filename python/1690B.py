# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = [ai - bi for ai, bi in zip(a, b)]
    if any(di < 0 for di in diff):
        print("NO")
    else:
        m = max(diff)
        print("YES" if all(di == m or bi == 0 for bi, di in zip(b, diff)) else "NO")
