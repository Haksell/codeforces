from collections import deque


for _ in range(int(input())):
    lower = deque()
    upper = deque()
    for i, c in enumerate(input()):
        if c.islower():
            if c != "b":
                lower.append((c, i))
            elif lower:
                lower.pop()
        else:
            if c != "B":
                upper.append((c, i))
            elif upper:
                upper.pop()
    res = []
    while lower or upper:
        d = (
            lower
            if not upper
            else upper
            if not lower
            else lower
            if lower[0][1] < upper[0][1]
            else upper
        )
        res.append(d.popleft()[0])
    print("".join(res))
