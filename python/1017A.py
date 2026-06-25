# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    a = [(i, *mir()) for i in rir()]
    a.sort(key=lambda t: sum(t[1:]), reverse=True)
    print(next(i for i, (id_, *_) in enumerate(a, 1) if id_ == 0))


if __name__ == "__main__":
    main()
