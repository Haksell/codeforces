# ruff: noqa: E731, E741
print(sum(1 if "+" in input() else -1 for _ in range(int(input()))))
