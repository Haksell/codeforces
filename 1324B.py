# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    d = dict()
    for i, n in enumerate(map(int, input().split())):
        if n in d and d[n] < i - 1:
            print("YES")
            break
        elif n not in d:
            d[n] = i
    else:
        print("NO")
