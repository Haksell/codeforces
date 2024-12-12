# ruff: noqa: E731, E741
def xor_reduction(n):
    if n & 3 == 0:
        return n
    elif n & 3 == 1:
        return 1
    elif n & 3 == 2:
        return n + 1
    else:
        return 0


for _ in range(int(input())):
    a, b = map(int, input().split())
    x = xor_reduction(a - 1)
    print(a if x == b else a + 2 if x ^ b == a else a + 1)
