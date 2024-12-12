# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    if n & 1:
        print(end="7")
        n -= 3
    print("1" * (n >> 1))
