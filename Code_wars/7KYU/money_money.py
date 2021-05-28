def calculate_years1(principal, interest, tax, desired):
    Y = 0
    while principal < desired:
        principal += (principal * interest) * (1 - tax)
        Y += 1
    return Y

def main():
    print(calculate_years1(1000, 0.05, 0.18, 1100))


if __name__ == "__main__":
    main()
