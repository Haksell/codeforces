# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    print("Kosuke" if n & 1 else "Sakurako")
