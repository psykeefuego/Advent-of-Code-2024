import re

with open("input.txt") as f:
    line="".join(x.strip() for x in f)

# Part 1
pattern=r"mul\((\d{1,3}),(\d{1,3})\)"
res=sum(int(a) * int(b) for a, b in re.findall(pattern, line))
print(res)

# Part 2
pattern=r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
res,flag=0,True
for a, b, c, d in re.findall(pattern,line):
    if len(d)>0:
        flag=False
    elif len(c) > 0:
        flag=True
    elif flag:
        res+=int(a)*int(b)
print(res)
