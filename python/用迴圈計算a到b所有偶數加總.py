a=eval(input())
b=eval(input())
sum=0
for i in range(a,b+1):
    if i % 2 ==0:
        sum=sum+i
print(sum)