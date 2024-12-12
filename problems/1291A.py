for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input()))
    e = [d for d in s if d & 1]
    print(-1 if len(e) < 2 else f"{e[0]}{e[1]}")