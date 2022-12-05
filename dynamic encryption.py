#Dynamic Encryption Testing
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
                if(a in e):
                    continue
                elif(chr(a) == d[len(d)-1]):
                    continue
                else:
                    e.append(str(a))
            stre += e[d.index(x)]
    print(stre)


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
    print(strd)


            
