linie = []



def wczytaj(file):
    with open(file) as plik:
        for linia in plik:
            for i in linia:
                print(i)


wczytaj("liczby.txt")




def factorof():
    factorial = 1
    for linia in linie:
        for k in linia:
            for d in range(1,k+1):
                factorial = factorial * d
                print(factorial)







factorof()