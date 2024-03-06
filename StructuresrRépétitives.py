# methode range(n,m-1,p)--->range(n,m-1)-->range(n,m-1,p)
#Boucle for  Le nomber  de repetation  peut etre connu
for i in range(1,6) :     # deux point et indentation 
 print(i)
 
for i in range(4) :     # deux point et indentation 
 print("Hello world")
 
 
for i in range(11) :     # deux point et indentation 
  print(i*7)
  
#example
s=0
for i in range(1,21) :
 n=int(input("entre un number "))
 s=s+n
print( " la somme est :  ",s)


#example 2
s=0
for i in range(1,21) :
 s=s+i
print( " la somme est : ",s)


# boucles imbriquées
#for i in sequnce1 :
#for j in sequnce2:

#example Multiplication

for i in range(1,11) :
    for j in range(1,11):
        print(i*j)

#example de Boucle imbriquees
l=int(input("entre la ligne "))
c=int(input("entre le collonnes"))
 for i in range(l):
     for j  in range(c):
         print("* ", end=" ")
     print()
#****************************************While************************
#exmple
# break (casse la boucle ) / continue (revient  au debut  de la boucle )                   
jeu_lance=True
print("*******")

while jeu_lance :
    choixMenu=input(">")
    if choixMenu == "again" :
        continue
    elif choixMenu == "quit" :
      break
    elif choixMenu=="hello":
        print("Bonjour ...")
    else :
        print("commande introuvable")  
print("a Bientot") 
    
    