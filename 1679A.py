# ruff: noqa: E731, E741
def ceil_div(numer, denom):
    return -(-numer // denom)


for _ in range(int(input())):
    n = int(input())
    if n < 3 or n & 1:
        print(-1)
    else:
        mini = ceil_div(n, 6)
        maxi = n // 4
        print(mini, maxi)
