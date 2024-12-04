n = int(input())
res = 0
for bill in (100, 20, 10, 5, 1):
    res += n // bill
    n %= bill
print(res)
