# ruff: noqa: E731, E741
if int(input()) >= 45:
    print("YES")
else:
    a = sorted(map(int, input().split()))
    print("YES" if any(x + y > z for x, y, z in zip(a, a[1:], a[2:])) else "NO")
