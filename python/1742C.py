# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    g = [input() for _ in range(8)]
    print("R" if "R" * 8 in g else "B")
