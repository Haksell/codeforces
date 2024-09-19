for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(ai & 1 for ai in a) in (0, n):
        print("YES")
        continue
    min_even = min(ai for ai in a if ai & 1 == 0)
    min_odd = min(ai for ai in a if ai & 1 == 1)
    print("YES" if min(a) & 1 and min_even > min_odd else "NO")
