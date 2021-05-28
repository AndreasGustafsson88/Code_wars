def is_pangram1(s):
    alphabet = set(letter.lower() for letter in s if letter.isalpha())
    return True if len(alphabet) == 26 else False

def is_pangram(s):
    alphabet = set()
    for letter in s:
        if letter.isalpha():
            alphabet.add(letter.lower())
    if len(alphabet) == 26:
        return True
    else:
        return False

def main():
    pangram = "The quick, brown fox jumps over the lazy dog!"
    print(is_pangram1(pangram))

if __name__ == "__main__":
    main()
