# ruff: noqa: E731, E741
import sys

n, m = map(int, input().split())
s = sys.stdin.read()
is_black_and_white = all(c.isspace() or c in "BGW" for c in s)
print("#Black&White" if is_black_and_white else "#Color")
