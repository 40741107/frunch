num=eval(input())
min_num=num
for i in range(2,11):
    if min_num>num:
        min_num=num
    num=eval(input())
print("最小值是",min_num)