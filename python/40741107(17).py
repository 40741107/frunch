import random 
begin=1
end=100
s="y"
count=0
while(s=="y" or s=="Y"):
    count=count+1
    n=random.randint(begin,end)
    print("%d 電腦猜%d" % (count,n))
    a=eval(input("1.太大 2.太小 3.答對了!"))
    if (a==2):
        begin=n+1
    elif (a==1):
        end=n-1
    elif (a==3):
        print("恭喜你答對了!")
        h=input("是否要再玩一局 (Y/N)")
        if (h=="y" or h=="Y"):
            count=0
            begin=1
            end=100
        elif(h=="n" or h=="N"):
            break
    elif (a==0):
        break
    
    