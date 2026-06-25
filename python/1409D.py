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
        n, s = mir()
        digits = [0] + list(map(int, str(n)))
        t = sum(digits)
        if t <= s:
            print(0)
            continue
        for i in reversed(range(len(digits))):
            t -= digits[i] - 1
            digits[i] = 0
            digits[i - 1] += 1
            if digits[i - 1] != 10 and t <= s:
                final = int("".join(map(str, digits)))
                print(final - n)
                break


if __name__ == "__main__":
    main()
