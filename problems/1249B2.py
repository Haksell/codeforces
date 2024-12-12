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
        a = [x - 1 for x in mir()]
        cycle_lengths = [-1] * n
        for i, ai in enumerate(a):
            if cycle_lengths[i] != -1:
                continue
            cycle = [ai]
            while ai != i:
                ai = a[ai]
                cycle.append(ai)
            for ai in cycle:
                cycle_lengths[ai] = len(cycle)
        print(*cycle_lengths)


if __name__ == "__main__":
    main()
