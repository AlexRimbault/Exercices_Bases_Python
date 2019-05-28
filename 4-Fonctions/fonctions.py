#1

def nombre(nb):
    print(nb *5)

nombre(7)

#2

def nombres_pairs(liste = [1,2,3,4,5,6,7,8,9,10]):
    return(liste[1],liste[3],liste[5],liste[7])

nombres_pairs()

#3

def fib(nb):
	a, b = 0, 1
	while a < nb:
		print(a, end=' ')
		a, b = b, a + b
		print()

fib(100)

#4

#1

def voyelle():
    chaine = "Hello World"
    for lettre in chaine:
        if lettre in "aeiouy":
            print(lettre)

voyelle()

#2
#TODO

#3
#TODO

#5
#TODO

#6
#TODO

#7
#TODO

#8
#TODO



