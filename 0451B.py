from itertools import groupby

n = int(input())
a = list(map(int, input().split()))
b = [y - x > 0 for x, y in zip(a, a[1:])]
g = [k for k, _ in groupby(b)]
f = g.count(False)
if f == 0:
    print("yes")
    print(1, 1)
elif f == 1:
    fs = [i for i, x in enumerate(b) if not x]
    first = fs[0]
    last = fs[-1]
    a[first : last + 2] = a[first : last + 2][::-1]
    b = [y - x > 0 for x, y in zip(a, a[1:])]
    if all(b):
        print("yes")
        print(first + 1, last + 2)
    else:
        print("no")
else:
    print("no")
