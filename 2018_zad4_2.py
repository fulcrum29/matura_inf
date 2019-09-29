
linie = []

def wczytaj(file):
    with open(file) as plik:
        for linia in plik:
            linie.append(linia.strip())

def diff_letter(tekst):
    tmp_tab = []
    licznik = 0
    for k in range((ord('Z') - ord('A'))+1):
        tmp_tab.append(0)
    for t in range(len(tekst)):
        tmp_tab[ord(tekst[t])-ord('A')] += 1;
    for p in tmp_tab:
        if p > 0:
            licznik += 1
    return licznik

res = 0
res_max = 0
res_index = 0

str_tmp =""

wczytaj("sygnaly.txt")
str_tmp = linie[100]
res = diff_letter(str_tmp)

for l in range(len(linie)):
    str_tmp = linie[l]
    res = diff_letter(str_tmp)
    if res > res_max:
        res_max = res
        res_index = l

print(linie[res_index])
print(res_max)
