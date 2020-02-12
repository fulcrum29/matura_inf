numery =[]
flat_list = []
with open("dane.txt") as plik:
    for nr in plik:
        numery.append(nr.strip().split(' '))
for i in range(len(numery)):
    numery[i] = list(map(int, numery[i]))

c = 0
for n in range (len(numery)):
    #print(n)
    g = 319
    a = 0
    for p in range(0,160):
        #print(p)


        if numery[n][p] == numery[n][g]:

            #print(numery[n][p], numery[n][g])
            g = g - 1
            a = a + 1
        if a == 159:
            c = c + 1
print(c)







