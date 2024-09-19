for _ in range(int(input())):
    n = int(input())
    s = input()
    print(2 if "..." in s else s.count("."))
