from collections import Counter


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = Counter(a)
    m = cnt.most_common(1)[0][1]
    print(max(n & 1, m * 2 - n))
