# ruff: noqa: E731, E741
n, t = map(int, input().split())
s = input()
for _ in range(t):
    s = s.replace("BG", "GB")
print(s)
