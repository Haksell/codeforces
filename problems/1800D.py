# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    s = input()
    print(len(s) - sum(a == b for a, b in zip(s, s[2:])) - 1)
