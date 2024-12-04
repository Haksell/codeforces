nb = int(input())
b = sorted(list(map(int, input().split())))
ng = int(input())
g = sorted(list(map(int, input().split())))

res = 0
while b and g:
    if abs(b[-1] - g[-1]) <= 1:
        res += 1
        b.pop()
        g.pop()
    elif b[-1] > g[-1]:
        b.pop()
    else:
        g.pop()
print(res)
