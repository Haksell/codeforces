# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        cnt = [0] * n.bit_length()
        for i, ai in enumerate(a, 1):
            while ai & 1 == 0:
                ai >>= 1
                n -= 1
            bits = 0
            while i & 1 == 0:
                bits += 1
                i >>= 1
            cnt[bits] += 1
        if n <= 0:
            print(0)
            continue
        res = 0
        for i, c in reversed(list(enumerate(cnt))):
            if n <= i * c:
                print(res + (n + i - 1) // i)
                break
            n -= i * c
            res += c
        else:
            print(-1)


if __name__ == "__main__":
    main()
