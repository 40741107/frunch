even=0
odd=0
for i in range(0,10):
    a=eval(input())
    if a % 2 ==0:
        even=even+1
    else:
        odd=odd+1
print("偶數數字有",even,"個")
print("基數數字有",odd,"個")