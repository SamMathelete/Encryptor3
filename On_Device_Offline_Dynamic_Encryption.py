#On Device Offline Dynamic Encryption
#uses public and private key

import os
import random
d = []
e = []
d1 = []
e1 = []

for i in range(10):
    d1.append(str(i))
while len(e1)<len(d1):
    a = random.randint(0,9)
    if(str(a) in e1):
        continue
    elif(str(a) == d1[len(e1)]):
        continue
    else:
        e1.append(str(a))

def encrypt(file):
    f = open(file,'r')
    x = file[0:(len(file)-4)]+'_encrypted.txt'
    f1 = open(x, 'w+')
    stre = ''
    st = f.read()
    for x in st:
        if(x == '\n'):
            continue
        if(x not in d):
            d.append(x)
            while True:
                a = random.randint(100,999)
                if(chr(a) == x):
                    continue
                elif(str(a) in e):
                    continue
                else:
                    e.append(str(a))
                    break
    for x in st:
        if(x == '\n'):
            stre += '\n'
        else:
            stre += e[d.index(x)]

    dstr = ''
    estr = ''
    for x in d:
        dstr += x
    for y in e:
        estr += y
    publickey = ''
    for k in estr:
        publickey += e1[d1.index(k)]
    privatekey = ''
    for k in e1:
        privatekey += k

    f1.write('D:'+dstr+'\n')
    f1.write('PubKey:'+publickey+'\n')
    f1.write(stre+'\n')
    f1.write('END')
    f1.close()
    f.close()
    os.remove(file)
    print('Encryption Successful.')
    print('Private Key: ', privatekey)

def decrypt(file,privatekey):
    f = open(file, 'r')
    x = file[0:(len(file)-14)]+'.txt'
    f1 = open(x, 'w+')
    st = ''
    stre = ''
    strd = ''
    strd1 = ''
    dstr = ''
    estr = ''
    publickey = ''
    while True:
        st = f.readlines()
        if(st[-1] == 'END'):
            break
    for x in st:   
        if(x[0:2] == 'D:'):
            dstr = x[2:len(x)-1]
        elif(x[0:7] == 'PubKey:'):
            publickey = x[7:len(x)-1]
        elif(x == 'END'):
            break
        elif(x == ''):
            continue
        else:
            stre += x[0:len(x)-1]
            stre += '012'
    d = []
    e = []
    e1 = []
    for x in privatekey:
        e1.append(x)
    for x in publickey:
        y = d1[e1.index(x)]
        estr += y
    epr = ''
    for i in range(len(estr)):
        if((i+1)%3 == 0):
            epr += estr[i]
            e.append(epr)
            epr = ''
        else:
            epr += estr[i]
    for x in dstr:
        d.append(x)
    for i in range(len(stre)):
        if((i+1)%3 == 0):
            strd1 += stre[i]
            if(strd1 == '012'):
                strd += '\n'
            else:
                strd += d[e.index(strd1)]
            strd1 = ''
        else:
            strd1 += stre[i]
    f1.write(strd)
    f1.close()
    f.close()
    os.remove(file)
    print('Decryption Successful.')


def console():
    while True:
        cmd = input('command>>')
        if(cmd.lower() == 'encrypt'):
            enc = input('Enter file name: ')
            try:
                encrypt(enc)
            except:
                print('File not found!')
        elif(cmd.lower() == 'decrypt'):
            dec = input('Enter file name: ')
            pk = input('Enter Private Key: ')
            if(len(pk)!=10):
                print('Invalid Private Key!')
            else:
                try:
                    decrypt(dec,pk)
                except:
                    print('Incorrect file or Private Key!')
        elif(cmd.lower() == 'exit'):
            exit()
        else:
            print('Incorrect Command.')

console()
            
