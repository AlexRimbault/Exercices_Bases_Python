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
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for elements in x:
        for element in elements:
                print(element)

#5

x = [1,10,20,30,40,50]


a = b = 0
# calcul manière 1
a = sum(x)
print(a)

# calcul manière 2
for i in x:
    b += i
print(b)

#6

for i in reversed(range(6)):
    print(i)

#7

for i in range(1,10):
    if i > 3:
        break
        print(i)

#8

n_min = 1
n_max = 10
n_break = 3

for number in range(n_min,n_max):
    if number > n_break:
        break
    print(number)

#9

for i in range (1,10):
    if i == 3:
        continue
print(i)

i = 0


#10

ordi = ["apple", "asus", "dell", "samsung"]
i = 0

while i < len(ordi):
    print(ordi[i])
    i += 1

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