courses = ["Computer Science", "Math", "English","IT","Software Engineering"]
print(courses)
print(courses[0]) #Accessing the first element in an array
print(courses[3]) #Accessing the fourth element in an array
print(courses[-2])

#Looping through an array
for course in courses:
    print(course)

# Adding a new element in an array
courses.append("Python")
print(courses)

#Deleting an element in an array
courses.remove("IT")
print(courses)