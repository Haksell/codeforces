from heapq import nsmallest
import sys

for _ in range(int(input())):
    min_first = min_second = sys.maxsize
    sum_seconds = 0
    for _ in range(int(input())):
        input()
        first, second = nsmallest(2, map(int, input().split()))
        min_first = min(min_first, first)
        min_second = min(min_second, second)
        sum_seconds += second
    print(sum_seconds + min_first - min_second)
