a = int(input())
b = int(input())
print("YES" if eval(f"{a} + {b} == {a + b}".replace("0", "")) else "NO")
