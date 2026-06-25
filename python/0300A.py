# ruff: noqa: E731, E741
def extract_negative(a):
    neg = next(ai for ai in a if ai < 0)
    a.remove(neg)
    return neg


n = int(input())
a = list(map(int, input().split()))
a.remove(0)
neg1 = extract_negative(a)
print(1, neg1)
if sum(ai < 0 for ai in a) & 1:
    neg2 = extract_negative(a)
    print(n - 3, *a)
    print(2, 0, neg2)
else:
    print(n - 2, *a)
    print(1, 0)
