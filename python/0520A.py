# ruff: noqa: E731, E741
from string import ascii_lowercase

input()
print("YES" if set(input().lower()) >= set(ascii_lowercase) else "NO")
