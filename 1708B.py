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
        n, l, r = mir()
        res = []
        for i in range(1, n + 1):
            x = l + (-l % i)
            if x > r:
                print("NO")
                break
            res.append(x)
        else:
            print("YES")
            print(*res)


if __name__ == "__main__":
    main()
