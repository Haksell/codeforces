# ruff: noqa: E731, E741
s = input()
print(s.swapcase() if s.isupper() or s.swapcase().istitle() else s)
