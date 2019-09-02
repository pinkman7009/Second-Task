import numpy as np


r=int(input())

a=np.zeros((r,r))

for i in range(r):
    line_input=input()
    j=0
    for k in line_input.split():
        a[i,j]=int(k)
        j+=1

l=int(input())

ans=(r/l)*(r/l)

for i in range(0,r,l):
    for j in range(0,r,l):
        sum=0
        for t in range(i,i+l):
            for v in range(j,j+l):
                sum+=int(a[t,v])
        avg=int(sum/(l*l))
        for t in range(i,i+l):
            for v in range(j,j+l):
                a[t,v]=avg
print(ans)        
print(a)        