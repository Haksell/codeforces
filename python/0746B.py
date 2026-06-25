# ruff: noqa: E731, E741
n = int(input())
ciphertext = input()
plaintext = [None] * n
end = True
i = 0
for c in reversed(ciphertext):
    if end:
        plaintext[~i] = c
    else:
        plaintext[i] = c
        i += 1
    end = not end
print("".join(plaintext))
