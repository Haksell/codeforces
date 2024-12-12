# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = input()
    a = len(n)
    d = n[0]
    b = n >= a * d
    before = 9 * (a - 1)
    after = int(d) + b - 1
    print(before + after)
