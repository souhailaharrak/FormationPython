"""A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)"""

#Snake Case
#Each word is separated by an underscore character:
my_variable_name = "Python"

#Pascal Case :Each word starts with a capital letter:
MyVariableName = "Python1"


#Camel Case : Each word, except the first, starts with a capital letter:

myVariableName = "Python3"

#**************************************************************
#Global variables can be used by everyone, both inside of functions and outside.
#Example 
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()



#**************************************************
#Example
#Create a variable inside a function, with the same name as the global variable
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

