for _ in range(int(input())):
    s = input()
    z = s.count("0")
    o = len(s) - z
    print(min(o, z) - (o == z))
