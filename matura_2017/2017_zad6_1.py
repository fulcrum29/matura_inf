
numery =[]
flat_list = []
with open("dane.txt") as plik:
    for nr in plik:
        numery.append(nr.split(' '))
for lister in numery:
    for item in lister:
        flat_list.append(item.strip())

flat_list = list(map(int, flat_list))
print(flat_list)
print(len(flat_list))
print(max(flat_list))
print(min(flat_list))





