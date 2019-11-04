linie = []



def wczytaj(file):
    with open(file) as plik:
        for linia in plik:
            linie.append(linia.strip())


wczytaj("liczby.txt")

print(linie)
def onenumber():
    for linia in linie:
        return linia

def factorof():

    for linia in linie:
        b = 0
        for k in linia:
            if k == 0:
                k = 1
            factorial = 1

            for a in range(1,int(k)+1):
               factorial = factorial * a
            b += factorial
        if int(linia) == b:
            print(linia)
            print(b)




factorof()



