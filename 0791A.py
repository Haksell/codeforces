from math import log

a, b = map(int, input().split())
print(1 + int(log(b / a, 1.5)))
