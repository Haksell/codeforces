import sys
read = sys.stdin.readline
write = lambda x, end="\n": sys.stdout.write(x + end)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def f(l):
    if l:
        i = max(range(len(l)), key=l.__getitem__)
        n = Node(l[i])
        n.left = f(l[:i])
        n.right = f(l[i + 1:])
        return n


def g(t, d):
    if t:
        g(t.left, d + 1)
        z.append(d)
        g(t.right, d + 1)


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    z = []
    t = f(l)
    g(t, 0)
    print(*z)