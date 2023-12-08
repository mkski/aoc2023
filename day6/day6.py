import re

inp = open("test").read().splitlines()

times = map(int, re.findall(r"\d+", inp[0]))
distances = map(int, re.findall(r"\d+", inp[1]))

def get_distance(hold_for: int, length: int):
    return (length-hold_for) * hold_for

total = 1
for t, r in zip(times, distances):
    total *= sum([get_distance(h, t) > r for h in range(t)])
print(total)

time = int(re.sub(r"[A-z:\s]+", "", inp[0]))
distance = int(re.sub(r"[A-z:\s]+", "", inp[1]))

print(sum([get_distance(h, time) > distance for h in range(time)]))
