import random
ans="y"
while ans =="y":
      num=random.randint(1,100)
      guest=int(input("你猜什麼數字:"))
      print(num)
      while num!=guest and guest!=0:
          if guest > num:
              print("你猜的數字太大")
          elif guest < num:
              print("你猜的數字太小")
          guest=int(input("你猜什麼數字:"))
      if guest !=0:
         print("恭喜您,答對了!!!")
      else:
          break
      ans=input("你是否再玩一局(y/n)?")