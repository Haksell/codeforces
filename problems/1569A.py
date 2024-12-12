# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    s = input()
    l = next((i for i, (c1, c2) in enumerate(zip(s, s[1:])) if c1 != c2), None)
    if l is None:
        print(-1, -1)
    else:
        print(l + 1, l + 2)
