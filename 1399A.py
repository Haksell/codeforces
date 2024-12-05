# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    print("YES" if all(y - x <= 1 for x, y in zip(a, a[1:])) else "NO")
