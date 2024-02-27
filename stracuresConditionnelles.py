#conditions multiples
#and (et) or (ou) in/not in(dans/pas dans)
 
letrre_hassard =True
if not letrre_hassard:
  print("ok")
else:
    print("NOok")
 
 #conditionnelle simple
n1=float(input("entre un number1 "))
n2=float(input("entre un number2 "))

if n1>n2 :
    max=n1
else :
    max=n2

print("le max est ",  max)



#operateur ternaire permet de simplifier  la syntaxe de la stracture conditionnelle
#valeurSiVrai  if condition else ValeurSiFaux
age=int(input("entre votre age "))
msg="accepter " if age>=18 else "ne pas accepter "
print(msg)



#conditionnelles a choix multiple 
n2=float(input("entre un number2 "))
if n2 > 0 :
    print("cette nomber possitif ")
elif n2==0:
    print("null")
else :
print("cette nomber negatif")



#Exmple empriquen
t=int(input("entre temperateur "))
if   t<0 :
    print("Glace ")
else :
 if t>0 and t<100 :
        print("LIquid ")
 else :
    print("vapeur ")



#Exemple Multi choix
n=int(input ("entre le nom de jour "))
if n==1 :
    print("lundi ")
elif n==2 :
     print("lundi ")
elif n==3 :
     print("Mardi ")
elif n==4 :
     print("Mercredi")
elif n==5 :
     print("jeudi ")
elif n==6 :
     print("samedi")
elif n==7 :
     print("demanch")
else :
   print ("le number inccorecte") 
    
    
#example
a=float(input("n2 "))

if a % 2 ==0:
    print("Pair")
else :
    print("impaire")


    
