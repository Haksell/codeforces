# ruff: noqa: E731, E741
s1 = input()
s2 = input()
print(-1 if s1 == s2 else max(map(len, [s1, s2])))
