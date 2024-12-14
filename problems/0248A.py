# ruff: noqa: E731, E741
left_opened = left_closed = right_opened = right_closed = 0
for _ in range(int(input())):
    l, r = map(int, input().split())
    if l:
        left_opened += 1
    else:
        left_closed += 1
    if r:
        right_opened += 1
    else:
        right_closed += 1
print(min(left_closed, left_opened) + min(right_closed, right_opened))
