no1=0
no2=0
null=0
for i in range(5):
    a=eval(input())
    if a==1:
        no1=no1+1
    elif a==2:
        no2=no2+1
    else:
        null=null+1
    print("編號1 候選人得票數為",no1)
    print("編號2 候選人得票數為",no2)
    print("作廢票數為",null)

if no1>no2:
    print("編號1 候選人當選")
elif no2>no1:
    print("編號2 候選人當選")
else:
    print("沒人當選")