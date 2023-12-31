inp = open("input").read().splitlines()
seqs = [list(map(int, seq.split())) for seq in inp]

def next_value(s):
    if any(s):
        return s[-1] + next_value([s[i] - s[i-1] for i in range(1, len(s))])
    return 0

print(sum([next_value(s) for s in seqs]))
print(sum([next_value(s[::-1]) for s in seqs]))

i=open("input").read().split("\n")
q=[list(map(int,s.split()))for s in i]
n=lambda s:s[-1]+n([s[i]-s[i-1]for i in range(1,len(s))])if any(s)else 0
print(sum([n(s)for s in q]),sum([n(s[::-1])for s in q]))