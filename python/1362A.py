# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b = sorted(map(int, input().split()))
    q, r = divmod(b, a)
    if r != 0 or q & (q - 1) != 0:
        print(-1)
    else:
        n = q.bit_length() - 1
        print(-(-n // 3))
