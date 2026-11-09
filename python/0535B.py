s = input()
print(int(s.translate(str.maketrans("47", "01")), 2) + (1 << len(s)) - 1)
