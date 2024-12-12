# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    w = [ord(c) & 31 for c in input()]
    n = sum(w) - int(input())
    a = sorted(w)
    while n > 0:
        n -= a.pop()
    counter = Counter(a)
    ans = []
    for c in w:
        if counter[c] >= 1:
            ans.append(c)
            counter[c] -= 1
    print("".join(chr(c | 96) for c in ans))
