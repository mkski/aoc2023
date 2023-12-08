from collections import defaultdict
from math import prod

inp = open("input").read()

inp = inp.replace("\n", ".\n.")
inp = f".{inp}."
rowl = inp.index("\n")
inp = f"{'.'*rowl}\n{inp}\n{'.'*rowl}"
inp = inp.split("\n")

gears = defaultdict(list)

def check_number(n, r, c):
    bbox = [
        inp[r-1][c-len(n)-1:c+1],
        inp[r][c-len(n)-1:c+1],
        inp[r+1][c-len(n)-1:c+1]
    ]

    is_part = False
    for lr, _ in enumerate(bbox):
        for lc, localc in enumerate(bbox[lr]):
            if localc in "#$%&*+-/=@":
                is_part = True
            if localc == "*":
                gear_r = r + lr - 1
                gear_c = c - len(n) + lc - 1
                gears[(gear_r, gear_c)].append(int(n))

    return int(n) if is_part else 0

def main():
    current = ""
    total = 0
    for r, row in enumerate(inp):
        for c, col in enumerate(row):
            if col.isdigit():
                current = f"{current}{col}"
            else:
                if current:
                    total += check_number(current, r, c)
                current = ""
        if current:
            total += check_number(current)
            current = ""

    print(total)
    gear_total = 0
    for numbers in gears.values():
        if len(numbers) > 1:
            gear_total += prod(numbers)
    print(gear_total)


if __name__ == "__main__":
    main()