import sys
read = sys.stdin.readline
write = lambda x, end="\n": sys.stdout.write(x + end)


def f(n):
    t = n * (n - 1) >> 1
    for i in range(n):
        for j in range(i + 1, n):
            if n & 1 == 0 and i & 1 == 0 and j == i + 1:
                yield 0
            elif (j - i - 1) & 1:
                yield -1
            else:
                yield 1


for _ in range(int(input())):
    n = int(input())
    print(*f(n))

"""
5
2
3
4
5
6

1 o+-x
2 -ox+
3 +xo-
4 x-+o

1 ox-+-+
2 xo+-+-
3 +-ox-+
4 -+xo+-
5 +-+-ox
6 -+-+xo

1 -1 1 -1   1 -1 1   -1 1   -1
"""