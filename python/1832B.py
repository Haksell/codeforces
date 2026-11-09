from itertools import accumulate


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    rm_left = list(accumulate((a[2 * i] + a[2 * i + 1] for i in range(k)), initial=0))
    rm_right = list(accumulate(a[:~k:-1], initial=0))
    print(sum(a) - min(li + +ri for li, ri in zip(rm_left, reversed(rm_right))))
