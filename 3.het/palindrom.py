#/usr/bin/env python3

def is_palindrom(s):
    i = 0
    j = len(s) - 1
    while i < len(s) & j >= i:
        if (s[i] != s[j]):
            print("Nem palindrom")
            return
        i = i + 1
        j = j - 1
    print("Palindrom")
            
            
def main():
    s = "gorog"
    s1 = "valami"
    s2 = "kek"
    is_palindrom(s2)

if __name__ == "__main__":
    main()

