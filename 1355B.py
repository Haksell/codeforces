# ruff: noqa: E731, E741
import sys

output = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    e = sorted(map(int, sys.stdin.readline().split()))
    size = 0
    ans = 0
    for x in e:
        size += 1
        if size >= x:
            ans += 1
            size = 0
    output.append(ans)
sys.stdout.write("\n".join(map(str, output)))
