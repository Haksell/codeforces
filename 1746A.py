# ruff: noqa: E731, E741
for s in [*open(0)][2::2]:
    print("YNEOS"[max(s) < "1" :: 2])
