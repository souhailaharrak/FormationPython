#Python has no command for declaring a variable.
x=5
y="Python"
print(x)
print(y)


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#*********************************************************
# Casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0



#**********************************************
#Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))


#Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a

#*********************************************
#Many Values to Multiple Variables
#exmple
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables

x = y = z = "Python"
print(x)
print(y)
print(z)


#Unpack a Collection  Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)





