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
        n = ir()
        a = lmir()
        special = [False] * (n + 1)
        for i in range(n - 1):
            s = a[i]
            for j in range(i + 1, n):
                s += a[j]
                if s > n:
                    break
                special[s] = True
        print(sum(special[ai] for ai in a))


if __name__ == "__main__":
    main()
