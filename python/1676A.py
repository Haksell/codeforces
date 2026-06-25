# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    print("YES" if sum(map(ord, s[:3])) == sum(map(ord, s[3:])) else "NO")
