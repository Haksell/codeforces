# ruff: noqa: E731, E741

for _ in range(int(input())):
    s = input()
    zbefore = obefore = 0
    zafter, oafter = s.count("0"), s.count("1")
    ans = min(zafter, oafter)
    for c in s:
        if c == "0":
            zbefore += 1
            zafter -= 1
        else:
            obefore += 1
            oafter -= 1
        ans = min(ans, zbefore + oafter, zafter + obefore)
    print(ans)
