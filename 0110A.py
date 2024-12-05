# ruff: noqa: E731, E741
n = input()
x = sum(c in "47" for c in n)
print("YES" if x == 4 or x == 7 else "NO")
