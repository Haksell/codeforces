# ruff: noqa: E731, E741
n = int(input())

prog = []
maths = []
pe = []
for i, stud in enumerate(map(int, input().split()), 1):
    lst = prog if stud == 1 else maths if stud == 2 else pe
    lst.append(i)

num_teams = min(len(prog), len(maths), len(pe))
print(num_teams)
for i in range(num_teams):
    print(prog[i], maths[i], pe[i])
