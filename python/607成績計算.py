def compute(list,i):
    print("Student",i)
    print("#Sum",sum(list))
    print("#Average %.2f" % (sum(list)/len(list)))

print("The 1st student:")
list1=[]
for i in range(5):
    list1.append(eval(input()))
print("The 2nd student:")
list2=[]
for i in range(5):
    list2.append(eval(input()))
print("The 3rd student:")
list3=[]
for i in range(5):
    list3.append(eval(input()))
compute(list1,1)
compute(list2,2)
compute(list3,3)