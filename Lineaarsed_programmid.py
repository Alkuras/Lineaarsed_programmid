#Ülesanne 1
from random import randint


nimi = input("Mis su nimi on?")
vanus = int(input("Kui vana sa oled?"))
print(f"Tere Maailm! Tervitan sind {nimi}! Sa oled {vanus} aastad vana!")


#Ülesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(f"Muutuja {vanus} on {type(vanus)} tüübi")
print(f"Muutuja {eesnimi} on {type(eesnimi)} tüübi")
 print(f"Muutuja {pikkus} on {type(pikkus)} tüübi")
 print(f"Muutuja {kas_käib_koolis} on {type(kas_käib_koolis)} tüübi")

#Ülesanne 3


from random import * #Importeerime kõik funktsioonid, mis on random moodulis
from math import *

 laud =randint(1,100)
 print(f"Laual on {laud} kommi")
 võta = int(input("Kui palju komme tahad võtta?"))
 nüüd = laud - võta
 print(f"Laual on {nüüd} komme nüüd.")

#Ülesanne 4

 ümbermõõt = float(input("Sisesta puu ümbermõõdu:"))
 läbimõõt = float(ümbermõõt/pi)
 print(f"Puu läbimõõt on {läbimõõt}")

#Ülesanne 5

N = float(input("Sisesta üks pool ristküülikus meetris "))
M = float(input("Sisesta teine pool ristküülikus meetris "))
D2 = float((N**2)+(M**2))
D= float(sqrt(D2))
print(f"{D}") 