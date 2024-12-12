# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    q, r = divmod(a + b + c, 9)
    print("YES" if r == 0 and min(a, b, c) >= q else "NO")
