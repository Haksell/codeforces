TARGET = "vika"

for _ in range(int(input())):
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    idx = 0
    for col in zip(*grid):
        if TARGET[idx] in col:
            idx += 1
            if idx == len(TARGET):
                print("YES")
                break
    else:
        print("NO")
