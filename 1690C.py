# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))
    res = []
    last_fi = 0
    for si, fi in zip(s, f):
        res.append(fi - max(si, last_fi))
        last_fi = fi
    print(*res)
