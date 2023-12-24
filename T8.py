num=int(input("Enter number of student :"))
sum=0
min=20
max=0
for i in range (num):
    n=float(input("Enter mark programing :"))
    sum+=n
    if n>max:
        max=n
        if n<min:
            min=n
avg=sum/num
print("miangin :", avg ,"bishtarin :",max,"kamtarin",min)






