#Multiline Strings
#You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#Strings are Arrays

a = "Hello, World!"
print(a[1])


#Looping Through a String
for x in "python":
  print(x)
  
  
#String Length
a = "Hello, World!"
print(len(a))


#Check String
#Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("the" in txt)


#Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

