# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    a = input()
    b = input()
    x1 = 1 + abs(a.count("0") - b.count("0"))
    x2 = sum(ai != bi for ai, bi in zip(a, b))
    print(min(x1, x2))
