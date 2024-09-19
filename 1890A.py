from collections import Counter


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    print("YES" if len(c) == 1 or len(c) == 2 and min(c.values()) == n >> 1 else "NO")
