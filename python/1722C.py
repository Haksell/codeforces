# ruff: noqa: E731, E741
def f(words, set1, set2):
    return sum(
        0 if (w in set1) and (w in set2) else 1 if (w in set1) or (w in set2) else 3
        for w in words
    )


for _ in range(int(input())):
    input()
    a = input().split()
    b = input().split()
    c = input().split()
    sa = set(a)
    sb = set(b)
    sc = set(c)
    print(f(a, sb, sc), f(b, sc, sa), f(c, sa, sb))
