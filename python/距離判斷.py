x1=eval(input())
y1=eval(input())
x2=5
y2=6
a=((x1-x2)**2+(y1-y2)**2)**(0.5)
if a<=15:
    print("Inside")
elif a>15:
    print("Outside")