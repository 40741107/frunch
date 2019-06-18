while True:
    year=eval(input())
    if year==-9999:
        break
    else:
        if year % 4 ==0 and year % 100!=0 or year % 400==0:
            print(year,"這一年是閏年")
        else:
            print(year,"這一年不是閏年")