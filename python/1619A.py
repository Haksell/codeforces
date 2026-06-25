# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    half = len(s) // 2
    print("YES" if len(s) % 2 == 0 and s[:half] == s[half:] else "NO")
