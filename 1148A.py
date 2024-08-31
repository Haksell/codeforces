a, b, c = map(int, input().split())
print(2 * c + (a + b if a == b else 2 * min(a, b) + 1))
