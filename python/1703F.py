# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


class FenwickTree:
    def __init__(self, size):
        self.__len = size
        self.__tree = [0] * (size + 1)
        self.__sum = 0
        self.__mid = 1 << (len(self.__tree).bit_length() - 1)

    @staticmethod
    def from_list(data):
        instance = FenwickTree(len(data))
        for i, n in enumerate(data, 1):
            instance.__tree[i] += n
            j = i + (i & -i)
            if j <= instance.__len:
                instance.__tree[j] += instance.__tree[i]
            instance.__sum += n
        return instance

    def __len__(self):
        return self.__len

    def __getitem__(self, i):
        return self.prefix_sum(i + 1) - self.prefix_sum(i)

    @property
    def sum(self):
        return self.__sum

    def update(self, i, delta):
        i += 1
        self.__sum += delta
        while i <= self.__len:
            self.__tree[i] += delta
            i += i & -i

    def prefix_sum(self, i):
        res = 0
        while i > 0:
            res += self.__tree[i]
            i -= i & -i
        return res

    def suffix_sum(self, i):
        return self.__sum - self.prefix_sum(i)

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left)

    def nth(self, nth):  # requires all elements to be nonnegative
        if nth < 0 or nth >= self.__sum:
            return None
        i = self.__mid
        shift = i >> 1
        res = 0
        while True:
            if i > self.__len or self.__tree[i] > nth:
                i -= shift
            else:
                nth -= self.__tree[i]
                res = i
                i += shift
            if shift == 0:
                return res
            shift >>= 1


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        ft = FenwickTree(n)
        r = 0
        for i, ai in enumerate(a, 1):
            if ai < i:
                r += ft.prefix_sum(ai)
                ft.update(i, 1)
        print(r)


if __name__ == "__main__":
    main()
