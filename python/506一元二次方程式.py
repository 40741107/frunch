def compute(a,b,c):
    r=b**2-4*a*c
    if r<0:
       return None
    elif r==0:
        return -b/(2*a)
    else:
        ans1=(-b+r**0.5)/(2*a)
        ans2=(-b-r**0.5)/(2*a)
        return str(ans1)+","+str(ans2)
a=eval(input())
b=eval(input())
c=eval(input())
ans=compute(a,b,c)
if ans==None:
    print("Your equation has no root.")
else:
    print(ans)