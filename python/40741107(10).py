n=eval(input())
for i in range(n,0,-1):
    num=eval(input())
    tmp=num
    ans=0
    while tmp!=0:
        ans+=(tmp%10)
        tmp=tmp//10
    print('Sum of all digits of',num,'is',ans)