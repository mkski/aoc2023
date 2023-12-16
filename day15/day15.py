import re
steps = open("input").read().strip().replace("\n", "").split(",")


def HASH(s):
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value %= 256
    return value


def parse_step(s):
    return re.findall(r"([a-z]+)(-|=)(\d+)?", s)[0]


def get_lens(label, boxes):
    box = HASH(label)
    for i, b in enumerate(boxes[box]):
        if b[0] == label:
            return i


boxes = [[] for _ in range(256)]
total = 0

for step in steps:
    total += HASH(step)
    match s := parse_step(step):
        case label, "=", value:
            box = HASH(label)
            if (ind := get_lens(label, boxes)) is not None:
                boxes[box][ind] = (label, value)
            else:
                boxes[box].append((label, value))
        case label, "-", "":
            box = HASH(label)
            if (ind := get_lens(label, boxes)) is not None:
                boxes[box].pop(ind)

print(total)
part2 = 0
for i, box in enumerate(boxes, 1):
    for l, lens in enumerate(box, 1):
        part2 += i * l * int(lens[1])
print(part2)
