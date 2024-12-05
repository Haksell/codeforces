# ruff: noqa: E731, E741
s1 = input().lower()
s2 = input().lower()
print(-1 if s1 < s2 else 0 if s1 == s2 else 1)
