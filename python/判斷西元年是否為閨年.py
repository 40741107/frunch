a=eval(input())
if a%4==0 and a%100==0:
    print(a,"這一年是閨年")
elif a%100==0:
    print(a,"這一年不是閨年")
elif a%4==0:
    print(a,"這一年是閨年")
else:
    print(a,"這一年不是閨年")    