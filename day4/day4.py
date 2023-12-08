inp = open("input").read().split("\n")
copies = [1 for _ in range(len(inp))]
num_cards = len(copies)

total = 0
for n, line in enumerate(inp):
    _, numbers = line.split(": ")

    winning, mine = numbers.split(" | ")
    winning = set([i for i in winning.split(" ") if i])
    mine = set([i for i in mine.split(" ") if i])
    
    if count := len(winning & mine):
        total += 2**(count-1)

        for c in range(count):
            if n + c+1 < num_cards:
                copies[n+c+1] += copies[n]
            
print(total)
print(sum(copies))