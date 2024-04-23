#prototyp programu do obliczania oszczędności na emeryturę

#zdefiniowanie zmiennych
w = int(input("wiek: "))
p = str(input("Płeć: "))
k = int(input("ile odkłada miesięcznie: "))
b2b = str(input("Czy jesteś samozatrudniony: "))

#stałe
l_ike = float(23472) #limit składki ike
l_ikze = float(9388.80) #limit składki ikze
l_ikzeb2b = float(14083.20) #limit składki ikze dla samozatrudnionych
l_oipe = float(23472) #limit składki oipe

m_dage = float(73.4 - 60) #średnia długość życia mężczyzny
f_dage = float(81.1 - 60) #średnia długość życia kobiety

#operacje na zmiennych
n = 60 - w #ile lat do emerytury

x = 12 * k #roczne oszczędności przeznaczane na emeryturę
x1 = x 

l = l_ike + l_ikze + l_oipe
l_b2b = l_ike + l_ikzeb2b + l_oipe

if b2b == "tak":
    if l_b2b < x:
        x = l_b2b
else:
    if l < x:
        x = l

#Obliczenia

def eme(x, n):
    for i in range(n):
        temp = (x * 1.07)+x1
        x = temp
    return round(x, 2)

def kapital(x, n):
    for i in range(n):
        temp = x + x1
        x = temp
    return round(x, 2)

def emerytura(x, p):
    if p == "m":
        return round((x / m_dage / 12), 2)
    else:
        return round((x / f_dage / 12), 2)

#Wyniki
print("Oszczędności na emeryturę: ", eme(x, n))
print("Uzbierany kapitał: ", kapital(x, n))
print("Miesięczna emerytura: ", emerytura(eme(x, n), p))