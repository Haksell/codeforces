# ruff: noqa: E731, E741
from itertools import count, product
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def valid(p, n, x, y):
    for i in range(n):
        friends = {(i - 1) % n, (i + 1) % n}
        if i == x:
            friends.add(y)
        if i == y:
            friends.add(x)
        fx = {p[f] for f in friends}
        mx = next(i for i in count() if i not in fx)
        if mx != p[i]:
            return False
    return True


def naive(n, x, y):
    for m in count():
        for p in product(range(m + 1), repeat=n):
            if valid(p, n, x, y):
                return p


def smart(n, x, y):
    p = [i & 1 for i in range(n)]
    if n & 1:
        p[0] = 2
    if (x + 1) % n == y or (y + 1) % n == x:
        return p
    if n & 1:
        return p[n - x :] + p[: n - x]
    if x & 1 == y & 1:
        p[x] = 2
    return p


def main():
    for _ in rir():
        n, x, y = mir()
        print(*smart(n, x - 1, y - 1))


def test():
    for n in range(3, 21):
        for x in range(n):
            for y in range(x + 1, n):
                p = smart(n, x, y)
                if not valid(p, n, x, y):
                    print(p, n, x, y)
                    return


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
