from collections import deque


for _ in range(int(input())):
    n = int(input())
    a = deque(map(int, input().split()))
    while a and a[0] == 0:
        a.popleft()
    while a and a[-1] == 0:
        a.pop()
    print(a.count(0))
