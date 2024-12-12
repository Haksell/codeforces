# ruff: noqa: E731, E741
def solve(x):
    bit = x & (x - 1)
    return 3 if x == 1 else x + 1 if bit == 0 else x - bit


for _ in range(int(input())):
    x = int(input())
    print(solve(x))
