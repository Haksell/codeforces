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
        n = list(map(int, input()))
        for i in range(len(n) - 1):
            b = n[i]
            r = 0
            for j in range(1, 9):
                if i + j >= len(n):
                    break
                d = n[i + j] - j
                if d > b:
                    b = d
                    r = j
            if r == 0:
                continue
            for j in range(i + r, i, -1):
                n[j] = n[j - 1]
            n[i] = b
        print("".join(map(str, n)))


if __name__ == "__main__":
    main()
