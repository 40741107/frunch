def compute(x):
    if x>1:
        for i in range(2,x):
            if x%i==0:
                return False
            else:
                return True
    else:
        return False

x=eval(input())
ans=compute(x)
if ans==False:
    print("Not Prime")
else:
    print("Prime")