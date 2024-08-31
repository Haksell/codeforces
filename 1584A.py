from fractions import Fraction
import math

"""
With x = u:
1 + y/v = (u+y) / (u+v)
1 + y/v = u/(u+v) + y/(u+v)
1 + y/v - y/(u+v) = u/(u+v)
y/v - y/(u+v) = u/(u+v) - 1
y(u+v)/v(u+v) - yv/v(u+v) = u/(u+v) - 1
(y(u+v) - yv) / v(u+v) = u/(u+v) - 1
(y(u+v) - yv) = (u/(u+v) - 1) * v(u+v)
yu = (u/(u+v) - 1) * v(u+v)
y = (u/(u+v) - 1) * v(u+v) / u
y = (u/(u+v) - 1) * (v/u)(u+v)
y = (v/u)(u+v)*u/(u+v) - (v/u)(u+v)
y = (v/u)*u - (v/u)(u+v)
y = v - (v/u)(u+v)
"""

# Alternatively, use (x-y)(x+y) = x*x - y*y and print(-(u*u), v*v)

for _ in range(int(input())):
    u, v = map(Fraction, input().split())
    y_frac = v - (v / u) * (u + v)
    x = u.numerator * y_frac.denominator
    y = y_frac.numerator
    g = math.gcd(x, y)
    print(x // g, y // g)
