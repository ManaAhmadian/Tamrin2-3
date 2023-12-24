import random
l=int(input("Enter the lenght array:"))
n=[random.randint(0,100)]
for i in range(l):
    #n=[random.randint(0,100)]
    num=random.randint(0,100)
    if num!=n:
        n.append(num)
        print (n)
    else:
        print("next number")

    
