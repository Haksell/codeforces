# ruff: noqa: E731, E741
import sys

n = int(input())
s = sys.stdin.read().strip()
if "OO" in s:
    print("YES")
    print(s.replace("OO", "++", 1))
else:
    print("NO")
