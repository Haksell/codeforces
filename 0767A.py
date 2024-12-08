# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    a = lmir()
    seen = set()
    for ai in a:
        seen.add(ai)
        day = []
        while seen and n in seen:
            day.append(n)
            seen.remove(n)
            n -= 1
        print(*day)


if __name__ == "__main__":
    main()
