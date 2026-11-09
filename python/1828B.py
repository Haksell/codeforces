import math

for _ in range(int(input())):
    input()
    print(math.gcd(*[i - int(x) for i, x in enumerate(input().split(), 1)]))
