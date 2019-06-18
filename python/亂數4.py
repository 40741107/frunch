import random
fruit=['apple','蘋果','orange','橘子','papaya','木瓜','grape','葡萄','kiwi','奇異果']
#print(fruit[1],fruit[3],fruit[5],fruit[7],fruit[9])
r_c=random.randrange(1,10,2)
r_e=random.randrange(0,9,2)
question="請問英文單字"+fruit[r_e]+"是什麼意思?"
question=question+"(1) 蘋果 (2) 橘子 (3) 木瓜 (4) 葡萄 "
print(question)