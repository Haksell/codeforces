from itertools import count

for i in count(int(input()) + 1):
    if len(str(i)) == len(set(str(i))):
        print(i)
        break
