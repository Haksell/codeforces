# ruff: noqa: E731, E741
for _ in range(int(input())):
    _, m = map(int, input().split())
    print("YES" if sum(map(int, input().split())) == m else "NO")
