# ruff: noqa: E731, E741
def g(n, s):
    if s[0] == "0" or s[-1] == "0" or s.count("1") & 1:
        return "NO"

    a = []
    b = []
    na = nb = 0
    for c in s:
        if c == "1":
            if na + nb >= 3:
                a.append(")")
                b.append(")")
                na -= 1
                nb -= 1
            elif na == 0 or nb == 0:
                a.append("(")
                b.append("(")
                na += 1
                nb += 1
            elif len(a) + 1 != n and s[len(a) + 1] == "0":
                a.append("(")
                b.append("(")
                na += 1
                nb += 1
            else:
                a.append(")")
                b.append(")")
                na -= 1
                nb -= 1
        else:
            if na <= nb:
                a.append("(")
                b.append(")")
                na += 1
                nb -= 1
            else:
                a.append(")")
                b.append("(")
                na -= 1
                nb += 1
    return f"YES\n{''.join(a)}\n{''.join(b)}" if na == nb == 0 else "NO"


for _ in range(int(input())):
    n = int(input())
    s = input()
    res = g(n, s)
    print(res)
