input()
a = list(map(int, input().split()))
maxi = max(a)
print(sum(maxi - n for n in a))
