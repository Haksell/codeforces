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
        n = ir()
        a = input()
        b = input()
        dots = [i for i in range(n) if a[i] == "." or b[i] == "."]
        if len(dots) < 3:
            print(0)
            continue
        res = 0
        for i in range(dots[1], dots[-2] + 1):
            if a[i] == b[i] == ".":
                res += a[i - 1] == a[i + 1] == "x"
                res += b[i - 1] == b[i + 1] == "x"
        print(res)


if __name__ == "__main__":
    main()
