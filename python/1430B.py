from heapq import nlargest

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum(nlargest(k + 1, a)))
