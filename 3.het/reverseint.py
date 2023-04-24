#/usr/bin/env python3

def reverse_int(n, k):
    s = str(n)
    s1 = str(k)
    print(s[::-1])
    print(s1[::-1])

def main():
    n = 1977
    k = 12568
    reverse_int(n, k)
    

if __name__ == "__main__":
    main()