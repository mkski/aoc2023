inp = open("input").read().strip()
l = inp.index("\n")
grid = [list(r) for r in inp.split("\n")]

expand_rows = [r for r, row in enumerate(grid) if all(c == "." for c in row)]
expand_cols = [
    c for c in range(len(grid[0]))
    if all(grid[r][c] == "." for r in range(len(grid)))
]


def distance(g1, g2, expand=1):
    x1 = g1[1] + (len([ec for ec in expand_cols if ec < g1[1]]) * expand)
    x2 = g2[1] + (len([ec for ec in expand_cols if ec < g2[1]]) * expand)
    y1 = g1[0] + (len([er for er in expand_rows if er < g1[0]]) * expand)
    y2 = g2[0] + (len([er for er in expand_rows if er < g2[0]]) * expand)
    return abs(x1-x2) + abs(y1-y2)


galaxies = []
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == "#":
            galaxies.append((r, c))

pairs = []
for i, g1 in enumerate(galaxies[:-1]):
    for g2 in galaxies[i+1:]:
        pairs.append((g1, g2))

print(sum(distance(g1, g2) for g1, g2 in pairs))
print(sum(distance(g1, g2, expand=999_999) for g1, g2 in pairs))
