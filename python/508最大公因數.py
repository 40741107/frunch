def compute(x,y):
    if x>0 and y>0:
        mix=1
        k=2
        while k<=x and k<=y:
            if x % k==0 and y % k==0:
               mix=k
            k=k+1
        return mix

while True:
   x,y=eval(input())
   if x!=-9999:
       print(compute(x,y)) 
   else:
      break

    