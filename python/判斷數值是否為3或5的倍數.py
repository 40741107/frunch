a=eval(input())
if a%5==0 and a%3==0:
    print(a,"這個數字同時是3和5的倍數")
elif a%3==0:
    print(a,"這個數字是3的倍數")
elif a%5==0:
    print(a,"這個數字是5的倍數")
else:
    print(a,"這個數字不是3或5的倍數")