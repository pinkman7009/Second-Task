import sympy as sy
g=int(input())

ans=0
if sy.isprime(g):
    ans=1

else:
    while g>0:
        close=sy.prevprime(g)
        if g-close==1:
            g-=1
            close=sy.prevprime(g)
            g+=1
        ans+=1
        g=g-close
        if sy.isprime(g)==1:
            ans+=1
            break

print(ans)    
        
    

