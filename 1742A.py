# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if a + b + c == max(a, b, c) << 1 else "NO")
