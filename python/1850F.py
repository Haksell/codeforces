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
        cnt = [0] * (n + 1)
        res = [0] * (n + 1)
        for x in a:
            if x <= n:
                cnt[x] += 1
        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                res[j] += cnt[i]
        print(max(res))


if __name__ == "__main__":
    main()
