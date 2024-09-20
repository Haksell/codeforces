from heapq import heappop, heappush


for _ in range(int(input())):
    input()
    h = []
    res = 0
    for card in map(int, input().split()):
        if card > 0:
            heappush(h, -card)
        elif h:
            res += -heappop(h)
    print(res)
