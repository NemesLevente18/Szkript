#!/usr/bin/env python3

def magas_mely(s):
    me = 0
    ma = 0
    MELY = 'aáoóuú'
    MAGAS = 'eéiíöőüű'
    for c in s:
        for k in MAGAS:
            if(c == k):
                ma += 1
        for l in MELY:
            if(c == l):
                me += 1
    if (me == 0 and ma == 0):
        return "semmilyen"
    if (me > 0 and ma == 0):
        return "mely"
    if (me == 0 and ma > 0):
        return "magas"
    if (me > 0 and ma > 0):
        return "vegyes"
    
    
def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "PFFFFffffttt"]
    for w in words:
        print(w + " --> " + magas_mely(w))

#####################################

if __name__ == "__main__":
    main()