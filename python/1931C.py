from collections import deque

for _ in range(int(input())):
    n = int(input())
    a = deque(map(int, input().split()))
    if a[0] == a[-1]:
        x = a[0]
        while a and a[0] == x:
            a.popleft()
        while a and a[-1] == x:
            a.pop()
        print(len(a))
    else:
        start = next(i for i in range(n) if a[i] != a[0])
        end = next(i for i in reversed(range(n)) if a[i] != a[-1])
        print(min(n - start, end + 1))
