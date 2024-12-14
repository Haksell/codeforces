# ruff: noqa: E731, E741
s = input()
to_delete = next((i for i, c in enumerate(s) if c == "0"), 0)
print("".join(c for i, c in enumerate(s) if i != to_delete))
