#!/usr/bin/env python3

def test(szamok):
    szamok = sorted(szamok)
    a = len(szamok)
    if(a % 2 == 0):
        return (szamok[round(a/2)] + szamok[round((a/2)-1)])/2.00
    else:
        return szamok[round(a/2)] 

def main():
    
    print(test([1, 2, 3, 4, 5]) == 3)
    print(test([3, 1, 2, 5, 3]) == 3)
    print(test([3, 6, 20, 99, 10, 15]) == 12.5)
    print(test([1, 300, 2, 200, 1]) == 2)
    print(test([5, 10, 20, 15]) == 12.5)
    
#####################################

if __name__ == "__main__":
    main()