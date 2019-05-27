#BASES

#1

developpeur = "Python"
print(developpeur)

#2

age = 25
prenom = "Alexandre"
phrase = "Je suis " + prenom + " et j'ai " + str(age) + " ans"
print(phrase)


#3
age, prenom = 25, "Alexandre"
phrase = "Je suis " + prenom + " et j'ai " + str(age) + " ans"
print(phrase)

#4
nombre = 3
print(nombre*4)

#5

#nombre1 = 1
nombre1 = 1

#nombre2 = 2
nombre2 = nombre1 + 1
print(nombre2)

#nombre3 = 3
nombre2 += 1
print(nombre2)

#6

#nombre1 = 1
nombre1 = 1

#nombre2 = 0 
nombre2 = nombre1 - 1
print(nombre2)

#nombre3 = -1
nombre2 -= 1
print(nombre2)

#7

#nombre1 = 1
nombre1 = 1

#nombre2 = 1
nombre2 = nombre1 * 1
print(nombre2)

#nombre3 = 1
nombre2 *= 1
print(nombre2)

#8

#nombre1 = 1
nombre1 = 1

#nombre2 = 1 
nombre2 = nombre1 / 1
print(nombre2)

#nombre3 = 1
nombre2 /= 1
print(nombre2)

#9
a = 5
b = 7
a, b = b, a
print (a,b)

#10

#1
a = 7
b = 7
print(a,b)

#2
a = b = 7
print(a,b)

#3
a = 7
b = a
print(a,b)

#11

a = 10
print(a)

print(a/2)

print(a//2)

print(a%2)

print(a**2)

#12
prix_ht = input("Veuillez entrer un prix hors taxes: ")
prix_ht = int(prix_ht)
nb_articles = input("Veuillez entrer un nombre d'articles: ")
nb_articles = int(nb_articles)
tva = prix_ht * 0.20
prix_ttc = prix_ht * nb_articles + tva

print(prix_ttc)


#LES LISTES

#13

ma_liste = [4,5]
print(ma_liste)

#14

ma_liste2 = ["Hello", "World", 7 , 3]
print(ma_liste2)
print(ma_liste2[0])
print(type (ma_liste2[3]))

#15

x = [1,5]
y = [2,9]
z = x + y
print(z)

#16

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[4])
print (x[3:5])
print(x[2:8:2])
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
del(x[3:5])
print(x)

#17

x = ["ok", 4, 2, 78, "bonjour"]
print(x[4])
x[2] = "toto"
print(x)

#18

x = [0, 1, 2, 3, 4, 5]
print(x)

x = []
x.append(0)
x.append(1)
x.append(2)
x.append(3)
x.append(4)
x.append(5)
print(x)

#LES DICTIONNAIRES

#19

#19

x = {"key":"valeur","key2":"valeur2"}
print(x)
print(x["key"])
x ["titi"] = "toto"
x ["titi"] = "tata"
print(x)
x.pop("titi")
x.pop("key")
print(x)
y = {}
y = x
print(y)

#LISTES, DICTIONNAIRES, TUPLES

