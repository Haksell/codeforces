# ruff: noqa: E731, E741
def is_subsequence(haystack, needle):
    i = 0
    for c in haystack:
        if c == needle[i]:
            i += 1
            if i == len(needle):
                return True
    return False


n = input()
for i in range(0, 1000, 8):
    if is_subsequence(n, str(i)):
        print("YES")
        print(i)
        break
else:
    print("NO")
