name=input("Entre your name : ")
family=input("enter your family : ")
m=float(input("Enter your math mark:"))
e=float(input("Enter your economic mark:"))
b=float(input("Enter your biology mark:"))
gpa=m+e+b/3
print("GPA :",gpa)
if gpa>=17:
    print("excellent")
elif 12<=gpa<=16:
    print("normal")
elif gpa<11:
    print("rejected")      

