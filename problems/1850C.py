# ruff: noqa: E731, E741
for _ in range(int(input())):
    print("".join(c for _ in range(8) for c in input() if c != "."))
