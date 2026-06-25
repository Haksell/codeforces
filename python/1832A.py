# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    left = s[: len(s) >> 1]
    print("YES" if len(set(left)) >= 2 else "NO")
