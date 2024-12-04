diff = 0
for _ in range(int(input())):
    m, c = map(int, input().split())
    diff += (m > c) - (m < c)
print("Mishka" if diff > 0 else "Chris" if diff < 0 else "Friendship is magic!^^")
