def compute(a,x,y):
    for i in range(1,y+1):
        for j in range(1,x+1):
            print(a,end=" ")
        print()
        
a=input()
x=eval(input())
y=eval(input())

compute(a,x,y)