
tekst = "ALAMAKOTA"

linie = []

counter = 0
ile = 0

def count_sign(str, znak):
    count = 0
    for k in range(len(str)):
        if str[k] == znak:
            count = count + 1
    return count

def wczytaj(file):
    with open(file) as plik:
        for linia in plik:
            linie.append(linia.strip())


wczytaj("sygnaly.txt")

tmp_count = 0;
str_tmp =""

#for k in linie:
#    tmp_count = tmp_count + 1
#    if tmp_count % 40 == 0:
#        str_tmp += k[9]

for k in linie[39::40]:
        str_tmp += k[9]


print(str_tmp)

