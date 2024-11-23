# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

MOD = 998244353

# sequence = 1,2,5,19,102,682,5321,47071,464570
# delta = 1,3,14,83,580,4639,41750,417499 = https://oeis.org/A079752 + 1


def main():
    seq = [1]
    delta = 1
    for n in range(10**6):
        seq.append((seq[-1] + delta) % MOD)
        delta = ((n + 4) * delta - 1) % MOD
    if False:
        d = {(0, 1)}
        print(len(d))
        for i in range(8):
            nd = set()
            for t in d:
                inv = sum(aj > ai for i, ai in enumerate(t) for aj in t[:i])
                for i in range(len(t) + 1):
                    nd.add(t[:i] + (inv,) + t[i:])
            d = nd
            print(len(d))
    else:
        for _ in rir():
            n = ir()
            print(seq[n - 2])


if __name__ == "__main__":
    main()

"""
[0,1] 0

[0,0,1] 0
[0,1,0] 1

[0,0,0,1] 0
[0,0,1,0] 1
[1,0,1,0] 3
[0,1,1,0] 2
[0,1,0,1] 1

[]
"""
