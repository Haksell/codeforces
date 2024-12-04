n = int(input())
start, *a = map(int, input().split())
mini = maxi = start
res = 0
for perf in a:
    if perf < mini:
        mini = perf
        res += 1
    elif perf > maxi:
        maxi = perf
        res += 1
print(res)
