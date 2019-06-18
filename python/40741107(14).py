b=0
c=0
for i in range(1,1001):
    import random
    a=random.randint(1,2)
    if a==1:
        b=b+1
    else:
        c=c+1
print("正面:%d次 反面:%d次")
