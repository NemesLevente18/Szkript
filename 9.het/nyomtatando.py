#!/usr/bin/env python3


def main():
    oldalak: list[str] = input("Adja meg az oldalakat: ").split(",")
    alsofelso: list[str] = []
    kimenet: list[str] = []

    for o in oldalak:
        if "-" in o:
            alsofelso = o.split("-")
            for i in range(int(alsofelso[0]), int(alsofelso[1]) + 1):
                kimenet.append(i)
        else:
            kimenet.append(int(o))
    print(kimenet)


if __name__ == "__main__":
    main()
