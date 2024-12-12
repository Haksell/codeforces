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
        k = ir()
        a = lmir()
        s = [False] * (k + 1)
        for ai in a:
            q, r = divmod(k - 2, ai)
            if r == 0 and s[q]:
                print(ai, q)
                break
            s[ai] = True


if __name__ == "__main__":
    main()
