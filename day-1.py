# Historian Hysteria 

n1,n2=map(int,input().split())
l1=[int(digit) for digit in str(n1)]
l2=[int(digit) for digit in str(n2)]
l1.sort()
l2.sort()
ans=0
for i in range(len(l1)):
  ans+=abs(l1[i]-l2[i])
print(ans)
