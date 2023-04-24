#!/usr/bin/env python3

def valid(text, chars):
    
    if(len(chars) == 0):
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    else:
        chars = chars
    i = 0
    j = 0
    result = ""
    
    while(i < len(text)):
        while(j < len(chars)):
            if (text[i] == chars[j]):
               result += text[i]
            j += 1
        i += 1
    return result




def main():
    
    print(valid("Barking!", ""))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))
#####################################

if __name__ == "__main__":
    main()