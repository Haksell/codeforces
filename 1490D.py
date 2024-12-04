class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def f(a):
    if a:
        i = max(range(len(a)), key=a.__getitem__)
        n = Node(a[i])
        n.left = f(a[:i])
        n.right = f(a[i + 1 :])
        return n


def g(t, d):
    if t:
        g(t.left, d + 1)
        z.append(d)
        g(t.right, d + 1)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    z = []
    t = f(a)
    g(t, 0)
    print(*z)
