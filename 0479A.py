import sys

a, b, c = map(int, sys.stdin)
print(max(a + b + c, (a + b) * c, a * (b + c), a * b * c))
