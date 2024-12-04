xs = ys = zs = 0
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    xs += x
    ys += y
    zs += z
print("YES" if xs == ys == zs == 0 else "NO")
