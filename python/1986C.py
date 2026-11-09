from collections import Counter, deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    s = list(input())
    ind = Counter(map(int, input().split()))
    c = deque(sorted(input()))
    for k, v in sorted(ind.items()):
        for _ in range(v - 1):
            c.pop()
        s[k - 1] = c.popleft()
    print("".join(s))
