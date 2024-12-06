# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        read()
        a = lmir()
        x = a.pop()
        c = 1
        r = 0
        while a:
            while a and a[-1] == x:
                a.pop()
                c += 1
            if not a:
                break
            r += 1
            for _ in range(c):
                a.pop()
                if not a:
                    break
                c += 1
        print(r)


if __name__ == "__main__":
    main()
