n = int(input())
m = int(input())
print(m if n >= 27 else m % (1 << n))
