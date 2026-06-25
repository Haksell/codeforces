# ruff: noqa: E731, E741
for _ in range(int(input())):
    c1, c2 = [ord(c) - 97 for c in input()]
    print(25 * c1 + c2 - (c2 > c1) + 1)
