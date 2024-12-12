# ruff: noqa: E731, E741
q = qa = qaq = 0
for c in input():
    if c == "Q":
        q += 1
        qaq += qa
    elif c == "A":
        qa += q
print(qaq)
