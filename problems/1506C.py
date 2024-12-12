# ruff: noqa: E731, E741
def f(a, b):
    for size in range(len(a), -1, -1):
        for i in range(size, len(a) + 1):
            ss = a[i - size : i]
            if ss in b:
                return len(a) + len(b) - 2 * size


for _ in range(int(input())):
    a = input()
    b = input()
    print(f(a, b))
