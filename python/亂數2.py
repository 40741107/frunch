import random
fruit=['apple','蘋果','orange','橘子','papaya','木瓜','grape','葡萄','kiwi','奇異果']
#print(fruit[1],fruit[3],fruit[5],fruit[7],fruit[9])
r_c=random.randrange(1,10,2)
r_e=random.randrange(0,9,2)
if r_c>5:
    r_e=r_c-1
question="請問"+fruit[r_c]+"的英文單字是"+fruit[r_e]+"嗎 yes/no?"
ans=input(question)
if ans.lower()=="yes":
    if fruit[r_e]==fruit[r_c-1]:
         print("恭喜你,答對了")
    else:
        print("很抱歉,您答錯了,答案應為",fruit[r_c-1])
else:
    if fruit[r_e]!=fruit[r_c-1]:
        print("恭喜你,答對了")
    else:
        print("很抱歉,您答錯了,答案應為",fruit[r_c-1])
