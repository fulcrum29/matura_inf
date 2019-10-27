linie = []

l_index = 0

def wczytaj(file):
    with open(file) as plik: # wczytaj plik
        for linia in plik:
            linie.append(linia.strip()) # zapelnij tablica liniami z plikow bez koncowki nowej lini



def max_value(tekst):
    tmp_tab = []
    tmp_index2 = 1
    for k in tekst:
        tmp_tab.append(ord(k))
    #print(tekst)
   # print(tmp_tab)
    for i in (tmp_tab):
        index_value = tmp_index2
        while index_value < len(tmp_tab):
            value = i - (tmp_tab[index_value])
            index_value += 1
            if value > 10 or value < -10:
                return False
        tmp_index2 += 1
    return True






wczytaj('sygnaly.txt')






for l in range(len(linie)):
    val = max_value(linie[l])
    if val == True:

        print(l,".",linie[l])
