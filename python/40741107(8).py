a=int(input("請輸入數字:"))
b=int(input("請輸入數字:"))
c=int(input("請輸入數字:"))
if(a>b>c):
    print("%.0f" % a)
elif(b>a>c):
     print("%.0f" % b)
elif(c>a>b):     
    print("%.0f" % c)
elif(b>c>a):
    print("%.0f" % b)
elif(a>c>b):
    print("%.0f" % a)
elif(c>b>a): 
    print("%.0f" % c)