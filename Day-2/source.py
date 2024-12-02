import numpy as np

with open("input.txt") as f:
    arr=[[int(i) for i in l.split()] for l in f]

def is_safe(d):
    return len(d[(d>0) & (d<=3)]) == len(d) or len(d[(d<0) & (d>=-3)]) == len(d)

p1,p2=0,0
for a in arr:
    if is_safe(np.diff(a)):
        p1+=1
        p2+=1
    else:
        for i in range(len(a)):
            if is_safe(np.diff(a[:i]+a[i+1:])):
                p2+=1
                break
print(p1)
print(p2)
