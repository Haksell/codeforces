# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def query(i, j):
    print("?", i, j, flush=True)
    return ir()


def answer(kind):
    print("!", kind, flush=True)


def solve():
    n = ir()
    x = lmir()

    cnt = [0] * n
    for xi in x:
        cnt[xi - 1] += 1
    if all(cnt):
        start = x.index(1) + 1
        end = x.index(n) + 1
        q1 = query(start, end)
        q2 = query(end, start)
        answer("A" if q1 < n - 1 or q2 < n - 1 or q1 != q2 else "B")
    else:
        start = next(i + 1 for i in range(n) if not cnt[i])
        end = next(i + 1 for i in range(n) if cnt[i])
        q1 = query(start, end)
        q2 = query(end, start)
        answer("A" if q1 == 0 or q2 == 0 or q1 != q2 else "B")


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
