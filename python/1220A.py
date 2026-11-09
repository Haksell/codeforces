from collections import Counter

input()
c = Counter(input())
print(*([1] * c["n"] + [0] * c["z"]))
