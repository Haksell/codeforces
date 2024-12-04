from collections import deque

input()
d = deque(list(map(int, input().split())))
x = y = 0
is_x_turn = True
while d:
    maxi = d.popleft() if d[0] > d[-1] else d.pop()
    if is_x_turn:
        x += maxi
    else:
        y += maxi
    is_x_turn = not is_x_turn
print(x, y)
