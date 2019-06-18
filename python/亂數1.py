import random
fruit=['apple','蘋果','orange','橘子','papaya','木瓜','grape','葡萄','kiwi','奇異果']
#print(fruit[1],fruit[3],fruit[5],fruit[7],fruit[9])
r=random.randrange(1,10,2)
question="請問"+fruit[r]+"的英文單字是甚麼?"
ans=input(question)
if ans==fruit[r-1]:
    print("恭喜你,答對了")
else:
    print("很抱歉,您答錯了,答案應為",fruit[r-1])