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
        cnt = [0] * (n + 1)
        for ai in mir():
            cnt[ai] += 1
        print(sum(n >> 1 for n in cnt))


if __name__ == "__main__":
    main()
