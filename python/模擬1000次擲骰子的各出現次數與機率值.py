import random
y1=0
y2=0
y3=0
y4=0
y5=0
y6=0
for i in range(0,1000):
    x=(random.randint(1,6))
    if x==1:
        y1+=1
    if x==2:
        y2+=1
    if x==3:
        y3+=1
    if x==4:
        y4+=1
    if x==5:
        y5+=1
    else:
        y6+=1
a1=y1/1000
a2=y2/1000
a3=y3/1000
a4=y4/1000
a5=y5/1000
a6=y6/1000
print(y1,y2,y3,y4,y5,y6)
print(a1,a2,a3,a4,a5,a6)