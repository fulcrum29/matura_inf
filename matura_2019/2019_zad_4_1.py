import sys


linie = []




def wczytaj(file):
    with open(file) as plik:
        for linia in plik:
            if 1162261467 % int(linia) == 0: # maximum value of integer divided by 
                linie.append(linia.strip())




wczytaj("liczby.txt")
print(linie)
print(len(linie))


