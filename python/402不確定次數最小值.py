a=eval(input())
min_a=a
while a!=9999:
    if min_a>a:
        min_a=a
    a=eval(input())
print(min_a)