# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sorted(a)
    mini = min(a)
    print("YES" if all(ai == si or ai % mini == 0 for ai, si in zip(a, s)) else "NO")
