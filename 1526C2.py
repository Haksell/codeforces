from heapq import heappop, heappush

input()
tot = 0
h = []
for ai in map(int, input().split()):
    if tot + ai >= 0:
        heappush(h, ai)
        tot += ai
    elif h and ai > h[0]:
        tot -= heappop(h)
        heappush(h, ai)
        tot += ai
print(len(h))
