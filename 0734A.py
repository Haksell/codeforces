# ruff: noqa: E731, E741
input()
s = input()
d = s.count("D")
a = s.count("A")
print("Anton" if a > d else "Danik" if d > a else "Friendship")
