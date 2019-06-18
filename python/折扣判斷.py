a=eval(input())
if a>=8000 and a<18000:
    print("%.1f" % (a*0.95))
elif a>=18000 and a<=28000:
    print("%.1f" % (a*0.9))
elif a>=28000 and a<=38000:
    print("%.1f" % (a*0.8))
elif a>=38000:
    print("%.1f" % (a*0.7))