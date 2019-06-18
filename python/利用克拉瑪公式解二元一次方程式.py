a,b,c=int(input()),int(input()),int(input())
d,e,f=int(input()),int(input()),int(input())
if a*e-b*d==0:
    print("無解")
else: 
    x=(c*e-b*f)/(a*e-b*d)
    y=(a*f-c*d)/(a*e-b*d)
    print("x是:%.0f" % x)
    print("y是:%.0f" % y)