inp = open("locations").read().split("\n")

for line in inp:
    dmin, smin, size = tuple(map(int, line.split(" ")))