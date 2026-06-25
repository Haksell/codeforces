# ruff: noqa: E731, E741
def binary_diff(a, b):
    c = a ^ b
    return bin(c).count("1")


_, others, max_diff = map(int, input().split())
others = [int(input()) for _ in range(others)]
fedor = int(input())
print(sum(binary_diff(o, fedor) <= max_diff for o in others))
