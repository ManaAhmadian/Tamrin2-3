import math
w=float(input("youre weight(kg) :"))
h=float(input("youre height(m) :"))
bmi=w/h**2
#math.pow(h,2)
print(bmi)
if bmi<18.5:
    print("you have lost weight")
else:
   print("your weight is normal")
if bmi>35:
    print("you have over weight")





