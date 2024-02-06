import sys


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    res = 0
    for _ in range(n):
        ai, bi = map(int, sys.stdin.readline().split())
        res += ai > bi
    print(res)
