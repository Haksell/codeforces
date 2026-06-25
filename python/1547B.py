# ruff: noqa: E731, E741
from collections import deque

for _ in range(int(input())):
    s = [ord(c) - 97 for c in input()]
    if set(s) != set(range(len(s))):
        print("NO")
    else:
        d = deque(s)
        for i in reversed(range(len(s))):
            if d[0] == i:
                d.popleft()
            elif d[-1] == i:
                d.pop()
            else:
                print("NO")
                break
        else:
            print("YES")
