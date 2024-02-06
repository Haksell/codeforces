for _ in range(int(input())):
    n = int(input())
    s = input()
    print(len({s[i : i + 2] for i in range(n - 1)}))
