

#L'instruction input() transforme toujours l'entrée de l'utilisateur en une chaîne,
#peu importe ce que l'utilisateur saisit.

birth_year = input()
print(type(birth_year))

#L'instruction int() convertit n'importe quel type de valeur en un entier
x = "55" #x is a string
y = int(x) #y is an integer

height = int(input())
#**************************************
#L'instruction float() convertit les valeurs en floats.
a = 3
b = float(a)
print(b)


#x=2.5
b=str(x)
print(x)
print(type(b))