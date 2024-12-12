# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    eights = -(-n // 4)
    nines = n - eights
    print("9" * nines + "8" * eights)
