for _ in range(int(input())):
    a = int(input()) - 3
    c = min(25, a)
    a -= c
    b = min(25, a)
    a -= b
    print("".join(chr(x + 97) for x in (a, b, c)))
