#1

def nombre(nb):
    print(nb *5)

nombre(7)

#2

def nbp(liste_nb):
    liste_pairs = []
    for element in liste_nb:
        if element % 2 == 0:
            liste_pairs.append(element)

    return liste_pairs

a = nbp([1,2,3,4,5,6,7,8,9,10])
print(a)

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

voy = ["a", "e", "i", "o", "u", "y"]
def nbv(caracters):
    cpt = 0
    for c in caracters:
         if c in voy:
             cpt += 1

    return cpt

nbv("salut la compagnie") # => 7

#2
voy = ["a", "e", "i", "o", "u", "y"]
def nbv(caracters):
     cpt = 0
     enum = 0
     while enum < len(caracters):
         if caracters[enum] in voy:
             cpt += 1
         enum += 1

     return cpt

#3
def nbv(caracters):
 cpt = 0
 for c in caracters:
if c in "aeiouy":
cpt += 1
return cpt

#5
def facto(nb):
cpt = nb

while nb != 1:
nb -= 1
cpt *= nb

return cpt

4*3*2*1
    

#6
def factorielle(n):
	if n == 1 :
		return 1
	else:
		return n * factorielle(n-1)

x = factorielle(5)
print(x)

#7
def ma_fonction(*args):
    len(args)
    sum(args)


ma_fonction(1, 2, 3, 4, 5, 6, 7, 8, 9, 1345679)

#8
def premier_chiffre(x):
	x=abs(x)
	s=str(x)
	return s[0]

def frequence_premiers_chiffres(liste):
	d = {c:0 for c in range(1, 10)}
     d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
	for x in liste:
		c=premier_chiffre(x)
		if c!= 0:
			d[premier_chiffre(x)] += 1
	return d

l = [1, 4 ,9 ,16 ,25 ,36 ,49 ,64 ,100 ,121]
r = frequence_premiers_chiffres(l)
print(r)



