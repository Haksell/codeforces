# ruff: noqa: E731, E741
from itertools import count
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

S = "codeforces"


def main():
    n = ir()
    t = 1
    for repeats in count(2):
        for i in range(len(S)):
            if t >= n:
                print(
                    "".join(
                        c * (repeats if j < i else repeats - 1) for j, c in enumerate(S)
                    )
                )
                return
            t = t * repeats // (repeats - 1)


if __name__ == "__main__":
    main()
