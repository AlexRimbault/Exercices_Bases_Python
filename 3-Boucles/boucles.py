#boucle for

#1

for x in range(0,6):
    print(x)

#2

liste = ["Je", "suis", "développeur"]

for mot in liste:
    print(len(mot), mot)

#3

x = "anticonstitutionnellement"

for letter in x:
    print(letter)

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

n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
n6 = 6
n7 = 7
n8 = 8
n9 = 9
n10 = 10

for number in range(n1,n10):
    if number > n3:
        break
    print(number)

#9

for i in range (1,10):
    if i == 3:
        continue
print(i)

i = 0


#10
#TODO



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