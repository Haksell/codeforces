# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [min(ai, bi) for ai, bi in zip(a, b)]
    d = [max(ai, bi) for ai, bi in zip(a, b)]
    print("YES" if c[-1] == max(c) and d[-1] == max(d) else "NO")
