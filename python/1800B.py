# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    cnt_lo = [0] * 26
    cnt_hi = [0] * 26
    for c in s:
        o = (ord(c) & 31) - 1
        (cnt_hi if c.isupper() else cnt_lo)[o] += 1
    start = sum(min(lo, hi) for lo, hi in zip(cnt_lo, cnt_hi))
    swaps = sum(abs(lo - hi) >> 1 for lo, hi in zip(cnt_lo, cnt_hi))
    print(start + min(swaps, k))
