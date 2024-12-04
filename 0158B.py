from collections import Counter

n = int(input())
a = list(map(int, input().split()))
counter = Counter(a)

res = counter[4]
res += counter[3]
counter[1] = max(0, counter[1] - counter[3])
res += -(-(2 * counter[2] + counter[1]) // 4)
print(res)
