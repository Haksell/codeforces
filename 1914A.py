from collections import Counter


for _ in range(int(input())):
    n = int(input())
    s = input()
    c = Counter(s)
    print(sum(c[chr(64 + i)] >= i for i in range(1, 27)))
