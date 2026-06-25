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
        n, c = input().split()
        n = int(n)
        s = input()
        if all(map(c.__eq__, s)):
            print(0)
            continue
        for i in range(2, n + 1):
            if all(s[j - 1] == c for j in range(i, n + 1, i)):
                print(1)
                print(i)
                break
        else:
            print(2)
            print(n, n - 1)


if __name__ == "__main__":
    main()
