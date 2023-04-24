#/usr/bin/env python3
import sys

def main():
    a = sys.argv[1] 
    b = sys.argv[2]
    n = input()
    k = input()
    
    print("Parancssori:", int(a) + int(b))
    print("Masik megoldas:", int(n) + int(k))
    
    

if __name__ == "__main__":
    main()