# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    print("YES" if all(s.index(c.lower()) < s.index(c) for c in "RGB") else "NO")
