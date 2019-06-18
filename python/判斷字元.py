a=input()
if ('0'<=a<='9'):
    print(a,"是數字")
elif ('a'<=a<='z' or 'A'<=a<='Z'):
    print(a,"是英文字母")
else:
    print(a,"是符號")