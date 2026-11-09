from itertools import count


for _ in range(int(input())):
    n = int(input())
    for i in count(2):
        if n % i:
            print(i - 1)
            break
