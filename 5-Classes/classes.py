#CLASSES

#1

class Carre:
    def __init__(self, cote):
        self.cote = cote


#3

class Carre:
    def __init__(self, cote):
        self.cote = cote
    def perimeter(self, perimetre):
        self.perimetre = perimetre
        return self.perimetre * self.cote

carre = Carre(7)
carre.perimeter(4)
print("Le périmètre total du carré est de", carre.perimeter(4), "cm")


#4

class Carre:
    def __init__(self, cote):
        self.cote = cote
    def perimeter(self, perimetre):
        self.perimetre = perimetre
        return self.perimetre * self.cote
    def area(self, aire):
        self.aire = aire
        return self.cote ** 2

carre = Carre(7)
carre.area(7)
print("L'aire totale du carré est de", carre.area(7),"cm")


#5

class Surcharge(Carre):
    def __init__(self,cote):
        Carre.__init__(self,cote)
    def perimeter(self,perimetre):
        Carre.perimeter(self,perimetre)
    def area(self,aire):
        Carre.area(self,aire)
    
print("Le carré à une longueur de", carre.cote, "cm,","une aire de", carre.area,"cm carré","et un périmètre de", carre.perimeter,"cm")


#6
#TODO

#7
#TODO

#8
#TODO

#9
#TODO

#10
#TODO

#11
#TODO

#12
#TODO


#2

if __name__ == "__main__":
    print(carre)
else:
    print("Script imported by another module")


#TESTS UNITAIRES

#1
#TODO

#2
#TODO

#3
#TODO

#4
#TODO