# ruff: noqa: E731, E741
s = input()
lo = sum(map(str.islower, s))
up = sum(map(str.isupper, s))
print(s.lower() if lo >= up else s.upper())
