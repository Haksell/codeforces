# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, m = map(int, input().split())
    x = input()
    s = input()
    for i in range(7):
        if s in x:
            print(i)
            break
        x *= 2
    else:
        print(-1)
