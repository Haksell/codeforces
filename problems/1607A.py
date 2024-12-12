# ruff: noqa: E731, E741
for _ in range(int(input())):
    k = input()
    s = input()
    print(sum(abs(k.index(c1) - k.index(c2)) for c1, c2 in zip(s, s[1:])))
