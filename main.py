# Feladat: Szövegelemzés és átalakítás
# Készíts egy Python programot, amely az alábbiakat végzi el:

# Szöveg bekérése a felhasználótól:
# Kérj be egy mondatot a felhasználótól. Például:

# Add meg a mondatot: Ma nagyon szép az idő.
# Szavak listába rendezése:
# Alakítsd a mondatot szavak listájává (a szóközök mentén).

# Szavak elemzése:

# Számold meg, hogy hány szó van a listában.
# Azonosítsd a leghosszabb szót, és írd ki a hosszát is.
# Átalakítás:

# Alakítsd át a szavak listáját úgy, hogy minden szót nagybetűssé alakítasz.
# Írd ki a szavak listáját egyesítve, vesszővel elválasztva.
# Rendezés:

# Rendezett sorrendben (ABC szerint) írd ki a szavakat.

from moduls import *

mondat=input('Adj meg egy mondatot!  ')

a=lista(mondat)

print(f'A mondatben: {len(a)} szó van')
print(f'A mondat leghosszabb szava: {max(a, key=len)}, {len(max(a,key=len))} betű.')
print(f'A mondat nagybetűvel: {nagy(mondat)}')
print(', '.join(a))
b=sorted(a)
print(b)



