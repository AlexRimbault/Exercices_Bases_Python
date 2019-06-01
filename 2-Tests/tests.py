#1

number1 = int(input("Veuillez entrer un premier nombre: "))
number2 = int(input("Veuillez entrer un deuxieme nombre: "))

if number1 * number2 > 0:
    print("Le produit de vos deux nombres est positif !")
elif number1 * number2 < 0:
    print("Le produit de vos deux nombres est négatif !")
else:
    print("Le produit de vos deux nombres est nul !")

#2

age = int(input("Veuillez entrer votre age: "))

if age >=18:
    print("Vous êtes majeur !")
else:
    print("Vous êtes mineur !")

#3

number = int(input("Veuillez entrer un nombre: "))

if number in range(6,9):
    print("Votre nombre est dans l'intervalle !")
else:
    print("Votre nombre n'est pas dans l'intervalle !")

#4

number = int(input("Veuillez entrer un nombre: "))

if 5 < number < 10:
    print("Votre nombre est dans l'intervalle !")
else:
    print("Votre nombre n'est pas dans l'intervalle !")

