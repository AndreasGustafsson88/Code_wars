def sum_dig_pow1(a, b):
    return [i for i in range(a, b + 1) if sum(int(d)**(j+1) for j, d in enumerate(str(i))) == i]



def sum_dig_pow(a, b):
    result = []
    for i in range(a, b + 1):
        if i > 9:
            sum = 0
            for j, num in enumerate(str(i)):
                sum += int(num)**(j+1)
            if sum == i:
                result.append(i)
        else:
            result.append(i)
    return result

def main():
    print(sum_dig_pow1(1, 100))


if __name__ == "__main__":
    main()
