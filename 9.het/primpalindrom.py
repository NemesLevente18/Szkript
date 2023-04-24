#!/usr/bin/env python3
MAX: int = 999999999


def is_palindrom(s: str):
    if s == s[::-1]:
        return True
    return False


def is_prime(n: int):
    szamlalo: int = 0
    for i in range(1, n + 1):
        if n % i == 0:
            szamlalo += 1
    return szamlalo


def test(n: int):
    for i in range(n, MAX):
        if is_prime(i) == 2 and is_palindrom(str(i)):
            return i


def main():
    print(test(31) == 101)
    print(test(130) == 131)
    print(test(131) == 131)
    print(test(1977) == 10301)
    print(test(11) == 13)


#####################################

if __name__ == "__main__":
    main()
