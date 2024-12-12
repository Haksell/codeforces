# ruff: noqa: E731, E741
def summands(n):
    lst = []
    power = 1
    while n > 0:
        n, units = divmod(n, 10)
        if units > 0:
            lst.append(units * power)
        power *= 10
    return lst


for _ in range(int(input())):
    lst = summands(int(input()))
    print(len(lst))
    print(*lst)
