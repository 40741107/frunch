n=eval(input())
sp=n-1
star=1
for i in range(0,n):
    for k in range(sp):
        print("",end=' ')
    sp=sp-1
    for s in range(star):
        print("*",end=' ')
    star=star+2
    print()