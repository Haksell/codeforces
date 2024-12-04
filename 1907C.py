from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = input()
    c = Counter(s).most_common(1)[0][1]
    if c + c <= n:
        print(n & 1)
    else:
        print(c + c - n)
