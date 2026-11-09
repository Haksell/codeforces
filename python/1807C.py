def f(s):
    even = set()
    odd = set()
    for i, c in enumerate(s):
        if c in even:
            if i & 1 == 1:
                return False
        elif c in odd:
            if i & 1 == 0:
                return False
        else:
            (odd if i & 1 else even).add(c)
    return True


for _ in range(int(input())):
    input()
    even = set()
    odd = set()
    print("YES" if f(input()) else "NO")
