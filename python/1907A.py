for _ in range(int(input())):
    a, b = input()
    for c in "abcdefgh":
        if a != c:
            print(c + b)
    for c in "12345678":
        if b != c:
            print(a + c)
