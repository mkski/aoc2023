import re
from math import prod

inp = open("input").read().strip("\n")

total = 0
power_total = 0

for line in inp.split("\n"):
    colors_max = [
        max([int(c) for c in re.findall(r"(?P<c>\d+) red", line)]),
        max([int(c) for c in re.findall(r"(?P<c>\d+) green", line)]),
        max([int(c) for c in re.findall(r"(?P<c>\d+) blue", line)]),
    ]
    power_total += prod(colors_max)

    if any([c > m for c, m in zip(colors_max, [12, 13, 14])]):
        continue
    total += int(re.search(r"Game (?P<id>\d+)", line).group("id"))
    
print(total)
print(power_total)