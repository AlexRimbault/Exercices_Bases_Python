#boucle for

#1

nombres = 0,1,2,3,4,5
for nombre in nombres:
    print(nombre)

#2

liste = ["I", "am", "legend"]
for mot in liste:
    print(mot, len(mot))

#3

x = "anticonstitutionnellement"
for lettre in x:
    print(lettre)

#4
#TODO



#5
#TODO

#6

for i in reversed(range(6)):
    print(i)

#7

for i in range(1,10):
    if i > 3:
        break
        print(i)

#8

nombre = 1,2,3,4,5,6,7,8,9,10
for nombre in range(1,10):
    if nombre > 3:
        break
        print(nombre)

#9

for i in range (1,10):
    if i == 3:
        continue
print(i)

#boucle while

#10
#TODO

ordi = ["apple", "asus", "dell", "samsung"]



#11

message = input("Veuillez saisir du texte: ")
while message != "exit":
        print(message)
        message = "exit" 

#12

i = -5

while i in range(-5,100):
        i +=5
        print(i)