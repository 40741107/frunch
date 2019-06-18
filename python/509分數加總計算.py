def compute(p,q):
    gcd=1
    k=2
    if p>0 and q>0:
        while p>=k and q>=k:
            if p % k ==0 and q % k==0:
                 gcd=k
            k=k+1
        return gcd

x,y=eval(input())
m,n=eval(input())
p=x*n+y*m
q=n*y
g=compute(p,q)
print("%.0f/%.0f+%.0f/%.0f=%.0f/%.0f" % (x,y,m,n,(p//g),(q//g)))