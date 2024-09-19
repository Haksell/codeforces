def solve(s):
    b0 = b1 = 0
    n0 = s.count("0")
    n1 = s.count("1")
    res = len(s)
    for i, c in enumerate(s):
        b0 += c == "0"
        b1 += c == "1"
        if n0 >= b1 and n1 >= b0:
            res = len(s) - i - 1
    return res


for _ in range(int(input())):
    s = input()
    print(solve(s))
