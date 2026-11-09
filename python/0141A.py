from collections import Counter

a, b, c = (input() for _ in range(3))
print("YES" if Counter(a) + Counter(b) == Counter(c) else "NO")
