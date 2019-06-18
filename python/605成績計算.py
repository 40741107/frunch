lt=[]
for a in range(10):
    lt.append(eval(input()))
lt2=sorted[lt]
ss=0
for i in range(1,9):
    ss=ss+lt2[i]
print(ss)
print("{:.2f}".format(ss/8))