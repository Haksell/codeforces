from statistics import median_high


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(median_high(a))
