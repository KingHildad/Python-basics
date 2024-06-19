# Inbuilt functions/standard library functions

y = min( 23, 56, 1000, 5647)
print(y)

x = max( 90, 6, 67, 47)
print("The max number is",x)

z = pow(2, 3)
print(z)

# user defined functions
def school():
     print("eMobilis")
school() # Calling a function
def multiply():
    num1 = 5
    num2 = 6
    print(num1*num2)
multiply()

# parameters and arguments
def add(a, b):
    print(a+b)
add(5,6)
add(10,6)
add(98,6)
add(54,6)

def Emloyee(fullname,age,salary,position):
    print(fullname,age,salary,position)
Emloyee("Jack Williams",23,56,100)
Emloyee("Liam liason",27,80000,100)
Emloyee("Alfred williams",28,76000,100)
Emloyee("Buck Kimani",32,67000,100)
Emloyee("Victor maiyani",18,10000,100)
