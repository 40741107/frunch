ss=0
for i in range(5):
    a=input()
    if a=='J':
       num=11
    elif a=='Q':
       num=12 
    elif a=='K':
       num=13
    elif a=='A':
       num=1
    else:
        num=eval(input())
    ss=ss+sum
print(ss)