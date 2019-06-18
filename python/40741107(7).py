num=int(input("請輸入年齡"))
if(num<6):
    print("可看普遍級")
elif(num<12):
    print("可看普遍級及保護級")
elif(num<18):
    print("可看限制級以外的所有影片!")
else:
    print("您已成年，可看各級影片")
  