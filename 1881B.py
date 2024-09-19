def solve(a, b, c):
    if b % a != 0 or c % a != 0:
        return False
    nb = b // a - 1
    nc = c // a - 1
    return nb + nc <= 3


for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    print("YES" if solve(a, b, c) else "NO")
