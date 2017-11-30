age = input("Enter Your Age:")
name = input("Enter Your Name:")
location = input("Enter Your Location:")

print("Age:" + age)
print("Name:" + name)
print("Location:" + location)

dateofyear = (int(age) - int(2017))
print("Hi "+ str(name) +" Your birth year: " + str(dateofyear)+" and your are from "+ str(location))
