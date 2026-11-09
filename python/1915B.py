for _ in range(int(input())):
    print(chr(657 - sum(ord(c) for _ in range(3) for c in input())))
