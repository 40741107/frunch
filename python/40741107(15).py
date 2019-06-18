import random
a=random.randint(1,100)
b=random.randint(1,100)
for i in range(a,b):
    b=int(input("電腦猜數字"))
    if b>a:
        print("你猜的數字太大")
    elif b<a:
        print("你猜的數字太小")
    elif b==a:
        print("恭喜您,答對了!!!")
        e=input("你還要再玩一局嗎?")
        if e=="要":
