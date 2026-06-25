# ruff: noqa: E731, E741
s = input()
a = s.count("a")
print(min(len(s), 2 * a - 1))
