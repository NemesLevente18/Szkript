#!/usr/bin/env python3

import math

def main():
    a = ['auto', 'villamos', 'metro']
    b = ['aladar', 'bela', 'cecil']
    c = [0] * 10
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    e = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    f = "1234567"
    g = 'The quick brown fox jumps over the lazy dog'
    h = "python is an awesome language"
    i = 'The quick brown fox jumps over the lazy dog'
    j = []
    k1 = []
    k2 = []
    l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    m = [' apple    ', '   banana   ', '  kiwi   ']
    n = [1, 0, 1, 1, 0, 1, 0, 0]
    t = []

    for s in a:
        print(s + " --> " + s.upper() + "!", end="   ")
    print()
    
    
    for s in b:
        print(s + " --> " + s.capitalize(), end="   ")
    print()
    
    
    print(c)
    
    
    for q in d:
        t.append(q*2)
    print(str(d) + " --> " + str(t))        
    
    
    t.clear()
    for q in e:
        t.append(int(q))
    print(str(e) + " --> " + str(t))
    
    
    p = []
    for s in list(f):
        p.append(int(s))
    print(str(f) + " --> " + str(p))
    
    
    hossz = []
    for w in g.split(" "):
        hossz.append(len(w))
    print(hossz)
    
    
    kezdo = []
    for w in h.split(" "):
        kezdo.append(w[0])
    print(kezdo)
    
    
    sok = []
    champ = ("", 0)
    for w in i.split(" "):
        # sok.append("(" + w + ", " + str(len(w)) + ")")
        champ = w, len(w)
        sok.append(champ)
    print(sok)
    
    
    for x in range(0, 10, 2):
        j.append(x)
    print(str(j))
    
    
    op = []
    for x in range(0, 20):
        k1.append(pow(x, 2))
    for x in k1:
        if(x % 2 == 0):
            op.append(x)
    print(op)
    
    
    for x in op:
        if(str(x).endswith('4')):
           k2.append(x) 
    print(k2)
    
    
    vmi = ''
    for s in l:
        vmi += s
    print(vmi)
    
    
    szo = []
    for s in m:
        szo.append(s.strip())
    print(str(m) + " --> " + str(szo))
    
    
    fuzott = ''
    for i in n:
        fuzott += str(i)
    print(str(n) + " --> " + fuzott)
    
    
#####################################

if __name__ == "__main__":
    main()