def iq_test(numbers):
    even = [int(i) for i, eni in enumerate(numbers.split(), 1) if int(eni) % 2 == 0]
    udda = [int(i) for i, eni in enumerate(numbers.split(), 1) if int(eni) % 2 != 0]

    return even[0] if len(even) < len(udda) else udda[0]


def iq_test1(numbers):
    list1 = numbers.split()
    even = []
    odd = []
    for i, enu in enumerate(list1):
        if int(enu) % 2 == 0:
            even.append(i + 1)
        else:
            odd.append(i + 1)
    if len(even) > len(odd):
        return odd[0]
    else:
        return even[0]


def main():
    print(iq_test("2 4 7 8 10"))


if __name__ == "__main__":
    main()
