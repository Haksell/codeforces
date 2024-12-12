for _ in range(int(input())):
    print("YNEOS"[eval(input().replace(" ", "-")) == 1 :: 2])