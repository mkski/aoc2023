import re

MapRange = tuple[int,int,int]

inp = open("test").read()
seedline, inp = inp.split("\n", 1)
map_ranges = inp.split("\n\n")

seeds = list(map(int, seedline.split(" ")[1:]))
seed_ranges = [
    tuple(map(int, r.group(1, 2)))
    for r in re.finditer(r"(\d+) (\d+)", seedline)
]

def get_dest(source: int, ranges: list[MapRange]) -> int:
    for dmin, smin, size in ranges:
        if smin <= source < smin + size:
            return dmin + (source - smin)
    return source

def get_dest_range(source_range: tuple, ranges: list[MapRange]) -> tuple:
    source_start, source_size = source_range
    final_start, final_size = source_start, source_size

    for dmin, smin, size in ranges:
        if smin <= source_start < smin+size:
            return dmin, dmin+size
    return source_start, source_size

def get_seed_location(seed: int) -> int:
    location = seed
    for m in map_ranges:
        _, ranges = m.strip().split("\n", 1)
        ranges = [
            tuple(map(int, n.split(" ")))
            for n in ranges.strip().split("\n")
        ]
        location = get_dest(location, ranges)
    return location

def get_seed_range_locations(seed_range: tuple):
    dest_range = seed_range
    for m in map_ranges:
        _, ranges = m.strip().split("\n", 1)
        ranges = [
            tuple(map(int, n.split(" ")))
            for n in ranges.strip().split("\n")
        ]
        dest_range = get_dest_range(dest_range, ranges)
        break
    return dest_range

print(min(get_seed_location(seed) for seed in seeds))
print(min(get_seed_range_locations(r) for r in seed_ranges))



# ----------------------------------------------------------------------
# part 2

# locations = []
# futures = []

# for n, seed_range in enumerate(re.finditer(r"(\d+) (\d+)", seedline)):
#     start, size = tuple(map(int, seed_range.group(1, 2)))
#     locations.append(get_seed_location(start+size))
    
# print(min(locations))
