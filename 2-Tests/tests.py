#1

n1 = input("Renseignez un premier nombre: ")
n1 = int(n1)

n2 = input("Renseignez un deuxieme nombre: ")
n2 = int(n2)

if n1 * n2 > 0:
    print("Le produit de vos deux nombres est positif")
elif n1 * n2 == 0:
    print("Le produit de vos deux nombres est nul")
else:
    print("Le produit de vos deux nombres est négatif")

#2

age = input("Veuillez renseigner votre âge: ")
age = int(age)

if age >=18:
    print("Vous êtes majeur")
else:
    print("Vous n'êtes pas majeur")

#3

nombre = input("Veuillez renseigner un nombre: ")
nombre = int(nombre)


if nombre > 5 and nombre < 10:
    print("Vrai")
else:
    print("Faux")

#4

nombre = input("Veuillez renseigner un nombre: ")
nombre = int(nombre)

if nombre < 5 or nombre > 10:
    print("Faux")
else:
    print("Vrai")
