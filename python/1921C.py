# ruff: noqa: E731, E741
for _ in range(int(input())):
    _, f, a, b = map(int, input().split())
    m = list(map(int, input().split()))
    tot = sum(min((y - x) * a, b) for x, y in zip([0] + m, m))
    print("YES" if tot < f else "NO")
