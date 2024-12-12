# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = input()
    print("YES" if any(s[:i] + s[n - 4 + i :] == "2020" for i in range(5)) else "NO")
