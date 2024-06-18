
d= int(input("Enter the base : "))
h = int(input("Enter the height : "))
x= float(0.5)
a = int(x * d * h)
print("The area of the trapesium is",a)


a= int(input("Enter Your First No : "))
b= int(input("Enter Your Second No : "))
c= int(input("Enter Your Third No : "))
if a > b > c:
    print(a,"is the largest number")
elif b > c > a:
    print(b,"is the largest number")
else:
    print(c,"is the largest number")
