import sys
read = sys.stdin.readline
write = lambda x, end="\n": sys.stdout.write(x + end)

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = min(l)
    print(sum(x != m for x in l))