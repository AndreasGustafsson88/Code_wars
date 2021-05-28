def disemvowel(string):
    vowels = ["a", "e", "i", "o", "u"]
    newstr = ""
    for letter in string:
        if letter.lower() in vowels:
            continue
        else:
            newstr += letter
    return newstr

def disemvowel1(string):

    return "".join([letter for letter in string if letter.lower() not in ["a", "e", "i", "o", "u"]])

def main():
    print(disemvowel("This website is for losers LOL!"))
    print(disemvowel1("This website is for losers LOL!"))


if __name__ == "__main__":
    main()
