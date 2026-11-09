for _ in range(int(input())):
    n = int(input())
    s = input()
    print(s.translate(str.maketrans("UD", "DU")))
