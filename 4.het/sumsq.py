#!/usr/bin/env python3

import math

def main():
    sum = 0
    pos = 0
    for x in range(1, 101):
        sum += pow(x, 2)
        pos += x
    pos = pow(pos, 2)
    print(pos - sum)
    
#####################################

if __name__ == "__main__":
    main()