inp = open("input").read().splitlines()
seqs = [list(map(int, seq.split())) for seq in inp]

def next_value(s):
    if any(s):
        return s[-1] + next_value([s[i] - s[i-1] for i in range(1, len(s))])
    return 0
    
def prev_value(s):
    if any(s):
        return s[0] - prev_value([s[i] - s[i-1] for i in range(1, len(s))])
    return 0

print(sum([next_value(s) for s in seqs]))
print(sum([prev_value(s) for s in seqs]))