a=eval(input())
b=eval(input())
c=eval(input())
if a<b and b<c:
    print(a,b,c)
elif a<b and c<b and a<c:
    print(a,c,b)
elif b<a and a<c:
    print(b,a,c)
elif b<a and c<a and b<c:
    print(b,c,a)
elif c<a and a<b:
    print(c,a,b)
elif c<a and b<a and c<b:
    print(c,b,a)