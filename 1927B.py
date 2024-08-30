from collections import defaultdict


for _ in range(int(input())):
    cnt = defaultdict(int)
    input()
    s = []
    for n in map(int, input().split()):
        cnt[n] += 1
        s.append(chr(cnt[n] | 96))
    print("".join(s))
