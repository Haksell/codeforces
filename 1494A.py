# ruff: noqa: E731, E741
def f(a, left, third):
    n = 0
    for c in a:
        if c == left or c == third:
            n += 1
        else:
            n -= 1
            if n < 0:
                return False
    return n == 0


for _ in range(int(input())):
    a = input()
    if a[0] == a[-1]:
        print("NO")
        continue
    left = a[0]
    right = a[-1]
    third = chr(198 - ord(left) - ord(right))
    print("YES" if f(a, left, third) or f(a, left, None) else "NO")
