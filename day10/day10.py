from collections import deque

inp = open("input").read()
s, l = inp.index("S"), inp.index("\n")
start = (s // l, s % (l+1))

grid = inp.splitlines()

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

# valid entries per pipe piece. we can "move" into the pipe if the move is valid
# for that piece.
# examples:
#   moving down DOWN into "|" is valid
#   moving left LEFT into "J" is invalid
entries = {
    "-": [RIGHT, LEFT],
    "|": [UP, DOWN],
    "L": [DOWN, LEFT],
    "J": [DOWN, RIGHT],
    "7": [RIGHT, UP],
    "F": [LEFT, UP],
}

# valid exits per pipe piece. we can "exit" the pipe if the move is valid
# for that piece.
# examples:
#   moving down DOWN out of "7" is valid
#   moving down DOWN out of "L" is invalid
exits = {
    "-": [RIGHT, LEFT],
    "|": [UP, DOWN],
    "L": [RIGHT, UP],
    "J": [LEFT, UP],
    "7": [LEFT, DOWN],
    "F": [RIGHT, DOWN],
}


def get_neighbors(pos: tuple[int, int]):
    r, c = pos
    if grid[r][c] == "S":
        # consider all neighboring positions for the start node
        neighbor_positions = [UP, LEFT, RIGHT, DOWN]
    else:
        # otherwise only consider valid exit nodes for the current position
        neighbor_positions = exits[grid[r][c]]

    neighbors = []
    for n in neighbor_positions:
        nr, nc = pos[0] + n[0], pos[1] + n[1]
        # ignore out of bounds or ground nodes
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        elif grid[nr][nc] == ".":
            continue
        # only add a neighbor if we can enter it from this position
        elif grid[nr][nc] == "S" or n in entries[grid[nr][nc]]:
            neighbors.append((nr, nc))
    return neighbors


def get_loop(start: tuple[int, int]):
    # build path in one direction from one of the starting neighbors
    # using two neighbors will build the path in multiple directions
    queue = deque([get_neighbors(start)[0]])
    # keep track of loop length at each node
    seen = {start: 0}

    # simple BFS search, quit when all valid neighbors have already been seen
    while queue:
        start = queue.popleft()
        neighbors = get_neighbors(start)
        queue.extend([n for n in neighbors if n not in seen])
        seen[start] = len(seen)

        if all(n in seen for n in neighbors):
            return seen


def count_inside(loop):
    # implementation of https://en.wikipedia.org/wiki/Nonzero-rule
    total = 0
    for r, row in enumerate(grid[:-1]):
        winding = 0
        for c, _ in enumerate(row):
            if (r, c) in loop and (r+1, c) in loop:
                # check if we moved vertically into or from this position
                diff = loop[(r,c)] - loop[(r+1, c)]

                # diff or 1 or -1 means the two positions are next to each other
                # in the loop path
                if diff not in [1, -1]:
                    # modulo loop length so first and last can appear next to each other
                    diff = diff % len(loop)

                # if diff is 1 or -1 then we're at an intersection and need to
                # increment or decrement the winding number
                winding += diff if diff in [1, -1] else 0

            # count the current position if we have a non-zero winding number
            # and the position isn't part of the loop
            total += winding and (r, c) not in loop
    return total


loop = get_loop(start)
print(len(loop) // 2)
print(count_inside(loop))
