from heapq import nlargest

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m1, m2 = nlargest(2, a + [0])
    print("YES" if m1 - m2 <= 1 else "NO")