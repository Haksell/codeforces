# ruff: noqa: E731, E741
input()
crimes = 0
officers = 0
for event in map(int, input().split()):
    if event == -1:
        if officers == 0:
            crimes += 1
        else:
            officers -= 1
    else:
        officers += event
print(crimes)
