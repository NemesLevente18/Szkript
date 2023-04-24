#!/usr/bin/env python3
def sliced(li: list[int]):
    utolso = 0
    for i in li:
        if i == 1:
            break
        utolso += 1
    return "".join(str(li)).replace(", ", "")[utolso + 1 : -1]


def bin2szr(n: int, hatvany: list[int]):
    bin: list[int] = []
    for i in hatvany:
        if i <= n:
            bin.append(1)
            n -= i
        else:
            bin.append(0)
    return bin


def is_palindrom(s: str):
    if s == s[::-1]:
        return True
    return False


def main():
    osszeg = 0
    masodik_hatvany: list[int] = sorted([2**i for i in range(20)], reverse=True)

    for k in range(1, 1000000):
        if is_palindrom(str(k)) and is_palindrom(sliced(bin2szr(k, masodik_hatvany))):
            osszeg += k
    print(osszeg)


#####################################

if __name__ == "__main__":
    main()
