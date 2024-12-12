# ruff: noqa: E731, E741
for i in range(4, 29):
    print("?", 1, i)
    x = int(input())
    if x == -1:
        print("!", i - 1)
        break
    print("?", i, 1)
    y = int(input())
    if x != y:
        print("!", x + y)
        break
