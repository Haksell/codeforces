# ruff: noqa: E731, E741
def f(n, x, odds):
    if odds == 0:
        return False
    if odds == n:
        return x & 1 == 1
    if x == n:
        return odds & 1 == 1
    return True


for _ in range(int(input())):
    n, x = map(int, input().split())
    odds = sum(int(o) & 1 for o in input().split())
    print("Yes" if f(n, x, odds) else "No")
