# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def smart(a):
    ones = []
    for ai in a:
        o = 0
        while ai and ai[-1] == 1:
            o += 1
            ai.pop()
        ones.append(o)
    ones.sort(reverse=True)
    r = 0
    while True:
        while ones and ones[-1] < r:
            ones.pop()
        if not ones:
            return r
        r += 1
        ones.pop()


def main():
    for _ in rir():
        n = ir()
        a = [lmir() for _ in range(n)]
        print(smart(a))


if __name__ == "__main__":
    main()
