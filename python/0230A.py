s, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
for strength, bonus in sorted(a):
    if strength >= s:
        print("NO")
        break
    s += bonus
else:
    print("YES")
