from collections import Counter

for _ in range(int(input())):
    input()
    print(sum(v // 3 for v in Counter(map(int, input().split())).values()))
