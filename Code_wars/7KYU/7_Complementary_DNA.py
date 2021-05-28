def DNA_strand(dna):
    d = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    return "".join([d[letter] for letter in dna])

def main():
    print(DNA_strand("ATTGC"))


if __name__ == "__main__":
    main()
