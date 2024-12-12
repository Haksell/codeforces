# ruff: noqa: E731, E741
def f(s):
    t = 0
    for c in s:
        if c == "T":
            t += 1
        elif t == 0:
            return False
        else:
            t -= 1
    return True


for _ in range(int(input())):
    n = int(input())
    s = input()
    print("YES" if s.count("M") == n // 3 and f(s) and f(s[::-1]) else "NO")
