# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = input()
    left = len(s.rstrip(")"))
    right = n - left
    print("Yes" if right > left else "No")
