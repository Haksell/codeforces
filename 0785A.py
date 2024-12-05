# ruff: noqa: E731, E741
SIDES = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}

print(sum(SIDES[input()] for _ in range(int(input()))))
