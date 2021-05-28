import random

pattern = (1, 10, 9, 12, 3, 4)


def thirt(n):
    toto, toto2 = n, 0
    while toto != toto2:
        toto2, toto = toto, 0
        for i, eni in enumerate(reversed(str(toto2))):
            toto += int(eni) * pattern[i % 6]

    return toto


def main():
    print(thirt(1111111111))
    for _ in range(5):
        print(random.randrange(1, 51))
    for _ in range(2):
        print(random.randrange(1, 11))

if __name__ == "__main__":
    main()
