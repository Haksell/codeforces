# ruff: noqa: E731, E741
import random
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(d, lr):
    q = []
    lo = hi = 0
    for i, (di, (l, r)) in enumerate(zip(d, lr)):
        if di == 1:
            lo += 1
            hi += 1
        elif di == -1:
            hi += 1
            q.append(i)
        if lo < l:
            x = l - lo
            for _ in range(x):
                if q:
                    d[q.pop()] = 1
            lo = l
        if hi > r:
            x = r - hi
            for _ in range(x):
                if q:
                    d[q.pop()] = 0
            hi = r
        if hi < lo:
            return
    for x in q:
        d[x] = 0
    return d


def main():
    for _ in rir():
        n = ir()
        d = lmir()
        lr = [tuple(mir()) for _ in range(n)]
        res = solve(d, lr)
        if res is None:
            print(-1)
        else:
            print(*res)


def is_valid(lr, res):
    if res is None:
        return True  # kinda
    x = 0
    for di, (l, r) in zip(res, lr):
        if di not in (0, 1):
            return False
        x += di
        if x < l or x > r:
            return False
    return True


def test():
    for _ in range(1000):
        n = random.randint(1, 10)
        d = random.choices([-1, 0, 1], k=n)
        lr = [random.choices(range(n + 1), k=2) for _ in range(n)]
        res = solve(d, lr)
        if not is_valid(lr, res):
            print(n, d, lr, res)
            return


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
