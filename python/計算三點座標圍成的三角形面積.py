x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())
x3=eval(input())
y3=eval(input())
side1=((x3-x2)**2+(y3-y2)**2)**0.5
side2=((x2-x1)**2+(y2-y1)**2)**0.5
side3=((x3-x1)**2+(y3-y1)**2)**0.5
s=(side1+side2+side3)/2
Area=(s*(s-side1)*(s-side2)*(s-side3))**(0.5)
print("三個座標圍成的三角形面積為:%.2f" % Area)