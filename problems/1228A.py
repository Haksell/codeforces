def f(n):
    s = str(n)
    return len(s) == len(set(s))


l, r = map(int, input().split())
print(next((i for i in range(l, r + 1) if f(i)), -1))