def comp1(array1, array2):
    try:
        return sorted(i ** 2 for i in array1) == sorted(array2)
    except:
        return False


def comp(array1, array2):
    if array1 and array2 is None:
        return False
    for i in array2:
        if i is None:
            return False
        return False if i ** 0.5 not in array1 else True


def main():
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
    a3 = [58, 85]
    a4 = [58 * 58, 85 * 85]
    print(comp(a3, a4))


if __name__ == "__main__":
    main()
