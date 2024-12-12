# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, s, t = map(int, input().split())
    both = s + t - n
    s -= both
    t -= both
    print(max(s, t) + 1)
