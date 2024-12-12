# ruff: noqa: E731, E741
a = input()
b = input()
print("YES" if a == b[::-1] else "NO")
