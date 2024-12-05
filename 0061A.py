# ruff: noqa: E731, E741
print("".join("0" if a == b else "1" for a, b in zip(input(), input())))
