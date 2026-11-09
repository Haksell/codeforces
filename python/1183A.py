from itertools import count

for n in count(int(input())):
    if sum(map(int, str(n))) & 3 == 0:
        print(n)
        break
