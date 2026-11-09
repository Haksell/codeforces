k, n, w = map(int, input().split())
price = k * w * (w + 1) // 2
print(max(0, price - n))
