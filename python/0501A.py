# ruff: noqa: E731, E741
def f(p, t):
    return max(p * 0.3, p - p * t / 250)


a, b, c, d = map(int, input().split())
m = f(a, c)
v = f(b, d)
print("Vasya" if v > m else "Misha" if m > v else "Tie")
