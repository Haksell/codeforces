# ruff: noqa: E731, E741
def f(a):
    n50 = n25 = 0
    for b in a:
        if b == 25:
            n25 += 1
        elif b == 50:
            if n25 == 0:
                return False
            n25 -= 1
            n50 += 1
        elif b == 100:
            if n50 >= 1 and n25 >= 1:
                n50 -= 1
                n25 -= 1
            elif n25 >= 3:
                n25 -= 3
            else:
                return False
    return True


input()
print("YES" if f(map(int, input().split())) else "NO")
