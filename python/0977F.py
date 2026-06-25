# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    read()
    a = lmir()
    ss = dict()
    for i, x in enumerate(a, 1):
        if x in ss:
            if x + 1 not in ss or len(ss[x + 1]) <= len(ss[x]):
                ss[x + 1] = ss[x]
                ss[x + 1].append(i)
            del ss[x]
        elif x + 1 not in ss:
            ss[x + 1] = [i]
    m = max(map(len, ss.values()))
    r = next(v for v in ss.values() if len(v) == m)
    print(m)
    print(*r)


if __name__ == "__main__":
    main()
