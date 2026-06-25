# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    print(1 << (n.bit_length() - 1))
