import re;s=re.sub;i=open("input").read().strip("\n")
print(sum([int(l[0]+l[-1])for l in s(r"[a-z]+","",i).split("\n")]))
for r in["one1","two2","three3","four4","five5","six6","seven7","eight8","nine9"]:i=i.replace(r[:-1],f"{r}{r[-2]}")
print(sum([int(l[0]+l[-1])for l in s(r"[a-z]+","",i).split("\n")]))
