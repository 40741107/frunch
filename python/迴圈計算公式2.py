n=eval(input())
sum=0
for i in range(n,1,-1):
    a=1/i
    sum=sum+a
sum=sum+1
print("總和:","%.6f" % sum)