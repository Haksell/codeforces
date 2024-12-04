r = range(int(input()))
a = []
b = []
for _ in r:
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
sa = sorted(r, key=a.__getitem__)
sb = sorted(r, key=b.__getitem__)
print("Poor Alex" if sa == sb else "Happy Alex")