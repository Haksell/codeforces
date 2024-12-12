# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    for y in range(2 * n):
        print("".join("." if (x ^ y) & 2 else "#" for x in range(2 * n)))
