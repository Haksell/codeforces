# ruff: noqa: E731, E741
def array_compression(a):
    b = sorted(range(len(a)), key=a.__getitem__)
    return sorted(range(len(b)), key=b.__getitem__)


for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    s = input()
    zeros = s.count("0")
    bad = [pi for pi, c in zip(p, s) if c == "0"]
    good = [pi for pi, c in zip(p, s) if c == "1"]
    bad = iter(array_compression(bad))
    good = iter(array_compression(good))
    ans = [next(bad) + 1 if c == "0" else next(good) + 1 + zeros for c in s]
    print(*ans)
