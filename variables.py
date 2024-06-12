# A variable is a container for storing a value.
number = 10
firstname = "Hildad"
lastname = "Muchiri"
school = "eMobilis"
num1 = 5
num2 = 7

print("My full name name is", firstname,lastname,"I study at",school)

print(firstname, lastname)
print(lastname)
total=(num1+num2)
print("The sum of",num1,"and",num2,"is", total)

#Data Types
number = 78 #Int
num = 0.25 #float
greeting = "How are you doing?" #str
isprogramminginteresting = True #bool
devices = ["laptop", "phone", "computer","tablet"] # List
browsers = ("Firefox","Chrome","Safari","Opera")  # Tuple
countries = {"Kenya","India","Germany"} # set
employee = {
    "firstname": "Hildad",
    "lastname": "Muchiri",
    "age": 23,
    "gender": "Male",
} # Dictionary
print(isprogramminginteresting)
print(countries)
print(num)
print(employee["firstname"])
print(devices[0])
print(browsers)
print(total)
print(type(countries))

#Type casting is the process of converting one data type to another

print(int(num),)
print(float(number))