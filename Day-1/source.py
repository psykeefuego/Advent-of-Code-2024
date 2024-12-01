# Historian Hysteria
from collections import Counter

with open("input.txt") as f:
    l=[[int(i) for i in l.split()] for l in f]

# part 1
l1,l2=[list(sorted(x)) for x in zip(*l)]
print(sum(abs(a-b) for a, b in zip(l1, l2)))

# part 2
ctr=Counter(l2)
print(sum(i*ctr[i] for i in l1))
