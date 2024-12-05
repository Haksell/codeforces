# ruff: noqa: E731, E741
t = ["T", "i", "m", "r", "u"]
for _ in range(int(input())):
    n = int(input())
    s = input()
    print("YES" if n == 5 and sorted(s) == t else "NO")
