# ruff: noqa: E731, E741
def counts(a):
    res = [0] * 26
    for ai in a:
        res[ai] += 1
    return res


for _ in range(int(input())):
    n = int(input())
    s = [ord(c) - 97 for c in input()]
    c0 = counts(s[(n & 1) << 1 :: 2])
    c1 = counts(s[1::2])
    res = n - max(c0) - max(c1)
    if n & 1:
        for i in range(n - 1):
            cnt = c0 if i & 1 else c1
            cnt[s[i]] += 1
            cnt[s[i + 1]] -= 1
            res = min(res, n - max(c0) - max(c1))
    print(res)
