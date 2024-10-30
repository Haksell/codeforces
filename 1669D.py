for _ in range(int(input())):
    n = int(input())
    s = input()
    print("YES" if all(len(set(b)) != 1 for b in s.split("W")) else "NO")
