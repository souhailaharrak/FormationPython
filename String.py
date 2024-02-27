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


#• les lettres minuscules ont une valeur ASCII supérieure à celle des lettres majuscules,
#max(),min()

nom="SOUHAILA"
for i in range(0,2) :
 print(nom[0:4],end=" ")
 
name="wissam "
for i in range(0,len(name),1):
    print(name[i])
    
name="salma"
for i in range(0,len(name),2):
    print(name[i],end=" ")
    print(i)


#• Recherche de sous-chaînes********

#• Find: recherche de la position d’une chaine dans une autre
s="welcom to python"
print(s.find("to")) 

#• Count: retourne ne nombre d’occurrence d’une chaine dans une autre
s="welcom to python"
print(s.count("a"))

#• endswith: vérifie si une chaine se termine par une autre
s="welcom to python"
print(s.endswith("a"))

#• startswith: vérifie si une chaine se commence par une autre
s="welcom to python"
print(s.startswith("we")) 