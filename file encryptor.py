#direct file encryptor
import os
import random
d = []
e = []

def encrypt(strn):
    stre = ''
    for x in strn:
        if(x in d):
            stre += e[d.index(x)]
        else:
            d.append(x)
            while len(e)<len(d):
                a = random.randint(100,999)
                if(str(a) in e):
                    continue
                elif(chr(a) == x):
                    continue
                else:
                    e.append(str(a))
            stre += e[d.index(x)]
    return stre

def filecryptor():
    file = input('Enter File Name(with extension): ')
    f = open(file,'r')
    ft = open('temp.txt','w+')
    a = f.read()
    ae = encrypt(a)
    ft.write(ae)
    f.close()
    ft.close()
    os.remove(file)
    os.rename('temp.txt', file)

def decrypt(stre):
    strd = ''
    strk = ''
    for i in range(len(stre)):
        if(i%3 == 2):
            strk += stre[i]
            strd += d[e.index(strk)]
            strk = ''
        else:
            strk += stre[i]
    return strd

def filedecryptor():
    file = input('Enter Encrypted File Name(with extension): ')
    f = open(file,'r')
    ft = open('temp.txt','w+')
    a = f.read()
    ae = decrypt(a)
    ft.write(ae)
    f.close()
    ft.close()
    os.remove(file)
    os.rename('temp.txt', file)

