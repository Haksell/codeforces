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
        stack = []
        for c in input():
            if stack and c == "B":
                stack.pop()
            else:
                stack.append(c)
        print(len(stack))


if __name__ == "__main__":
    main()