l=int(input("Enter the lenght array:"))
x=[]
for i in range(l):
    num=int(input("Enter number:"))
    x.append(num)
    #print(x)
y=x[:]
y.sort()
if y==x:
    print("sort",x,y)
else:
    print(" not sort",x,y)

   

