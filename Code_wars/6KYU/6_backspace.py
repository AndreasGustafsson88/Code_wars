import re

def clean_string(s):
    new_str = re.sub("\x08|#", "\b", s)

    return new_str

def clean_string(s):
    list1 = []
    for letter in s:
        if letter != "#":
            list1.append(letter)
        else:
            try:
                list1.pop()
            except:
                continue
    return "".join(list1)

def main():
    print(clean_string('"#1##{#JL#"#s@#8J>$d;##@^'))
    # Js8J>$@^
    print("abc\x08d\x08\x08c")

if __name__ == "__main__":
    main()
