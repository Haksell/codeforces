for _ in range(int(input())):
    n = int(input())
    neg = input().count("-")
    pos = n - neg
    if neg > pos:
        res = neg - pos + 1 >> 1
        neg -= res
    else:
        res = 0
    print(res + (neg & 1))
