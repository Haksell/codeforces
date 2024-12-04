import sys


def f(m, a, b):
    x = a.pop()
    ans = [x]
    d = x
    while a and b:
        if a and d + a[-1] < m:
            x = a.pop()
            d += x
            ans.append(x)
        else:
            x = b.pop()
            d -= x
            ans.append(-x)
    ans.extend(a)
    ans.extend([-x for x in b])
    return ans


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    maxi = max(a)
    mini = min(a)
    m = maxi - mini
    if m == 0:
        print("No")
        continue
    print("Yes")
    pos = sorted([x for x in a if x > 0])
    neg = sorted([-x for x in a if x < 0])
    ans = f(m, pos, neg)
    ans.extend([0] * (n - len(ans)))
    print(*ans)
