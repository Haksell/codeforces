# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    e = o = 0
    for i, n in enumerate(a):
        if i & 1 == 0 and n & 1 == 1:
            e += 1
        if i & 1 == 1 and n & 1 == 0:
            o += 1
    print(e if e == o else -1)
