from itertools import cycle,izip
##
x = [41, 12, 88, 3, 56, 28, 17, 93]
z = [83, 101, 55, 110, 111, 108, 100, 46, 74, 65, 54, 106, 93]
i,k,l = 0,0,0
a = []
b = []
q = []
w = []
msg = ""
print ("[+] converting to binary")
print ("x array in binary")
for i in range(len(x)):
    a.append(bin(x[i]))
print ("z array in binary")
for i in range(len(z)):
    b.append(bin(z[i]))
print (a)
print (b)

print ("[+] convert binary")
#print int(a[0],2)
for i in range(len(a)):
    q.append(int(a[i],2))
for i in range(len(b)):
    w.append(int(b[i],2))
#print q
#print w

print ("[+] xoring")
msg = [f^g for f, g in izip(w, cycle(q))]
p = []
for i in range(len(msg)):
    p.append(hex(msg[i]))
h = ""
for i in range(len(p)):
    h += p[i].replace('0x','')

print((h).decode('hex'))
