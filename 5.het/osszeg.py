#!/usr/bin/env python3

def main():
    n = 2**1000
    c = list(str(n))
    sum = 0
    for ch in c:
        sum += int(ch)
    print(sum)
    
#####################################

if __name__ == "__main__":
    main()