import re
from itertools import cycle
from functools import reduce
from math import lcm

steps, nodes = open("input").read().split("\n\n")
nodes = re.sub(r"[\(\) =,]+", "", nodes)
steps = list(map(int, steps.replace("L", "0").replace("R", "1")))
nodes = {
    node: [left, right]
    for node, left, right in re.findall(r"([A-Z]{3})([A-Z]{3})([A-Z]{3})", nodes)
}


def get_steps(start, check):
    node = start
    for count, step in enumerate(cycle(steps), 1):
        node = nodes[node][step]
        if check(node):
            return count


print(get_steps("AAA", lambda n: n == "ZZZ"))
distances = [
    get_steps(node, lambda n: n[-1] == "Z")
    for node in [n for n in nodes if n[-1] == "A"]
]
print(reduce(lcm, distances))