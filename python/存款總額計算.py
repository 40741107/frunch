a=eval(input())
b=a*(1+(0.0123/12))
c=(a+b)*(1+(0.0123/12))
d=(a+c)*(1+(0.0123/12))
e=(a+d)*(1+(0.0123/12))
f=(a+e)*(1+(0.0123/12))
g=(a+f)*(1+(0.0123/12))
print("六個月後存款總金額:%.2f" % g)