
linie = []

def wczytaj(file):
    with open(file) as plik: # wczytaj plik
        for linia in plik:
            linie.append(linia.strip()) # zapelnij tablica liniami z plikow bez koncowki nowej lini

def diff_letter(tekst):
    tmp_tab = []
    licznik = 0
    for k in range((ord('Z') - ord('A'))+1): # wypelnij tablice
        tmp_tab.append(0)
    for t in range(len(tekst)):
        tmp_tab[ord(tekst[t])-ord('A')] += 1
    for p in tmp_tab:
        if p > 0:
            licznik += 1
    return licznik


res_max = 0


str_tmp =""

wczytaj("sygnaly.txt")


for l in range(len(linie)):
    val = diff_letter(linie[l])
    if val > res_max:
        res_max = val
        str_tmp = linie[l]


print(res_max)
print(str_tmp)

#print(res_max)


#print(linie[res_index])
#print(res_max)
