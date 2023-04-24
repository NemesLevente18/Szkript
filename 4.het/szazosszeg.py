#!/usr/bin/env python3

#>>>   li=range(1,101)
#>>>   sum(li)

def main():
    li = range(1, 101)  #1-101-ig a szamok
    sum = 0
    for i in li:
        if (i >= 10):   #ha a szam nagyobb/egyenlo 10-el
            ki = list(str(i))   #stringet, majd listat csinalunk a karakterekbol
            for k in ki:
                sum+=int(k)     #int-e alakitjuk es hozzaadjuk az osszeghez
        else:
            sum+=i
    print(sum)

#################1############################################################

if __name__ == "__main__":
    main()