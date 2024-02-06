for _ in range(int(input())):
    input()
    char = None
    res = ""
    for i, c in enumerate(input()):
        if char is None:
            char = c
            res += char
        elif c == char:
            char = None
    print(res)
