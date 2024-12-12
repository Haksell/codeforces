# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        k, q = mir()
        a = lmir()
        m = min(a)
        n = lmir()
        print(*[min(m - 1, ni) for ni in n])


if __name__ == "__main__":
    main()
