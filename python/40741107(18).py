list=[]
for i in range(10):
    list.append(eval(input()))
maxc=0
for i in range(10):
    if list.count(list[i])>maxc:
        maxc=list.count(list[i])
        mnum=list[i]
print("眾數為:",mnum)
print("次數為:",maxc)