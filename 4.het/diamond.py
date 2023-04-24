#!/usr/bin/env python3

def main():
    print("Adja meg a gyemant magassagat: ", end="")
    szam = input()
    print()
    i = int(szam)
    if (i % 2 == 0):
        print("Hiba! Csak paratlan szamot adhatsz meg!")
        return
    for k in range(1, i + 1):
        k = k - (i//2 + 1)
        if(k < 0):
            k = -k
        print(" " * k + "*" * (i - k * 2) + " " * k)
    
    print()

#####################################

if __name__ == "__main__":
    main()