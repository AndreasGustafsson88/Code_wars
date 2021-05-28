def meeting(s):
    return "".join(f"({i[1]}, {i[0]})" for i in sorted([name.upper().split() for name in s.replace(":", " ").split(";")], key=lambda x: (x[1], x[0])))


def main():
    folk = "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Aan:Arno;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
    print(meeting(folk))

if __name__ == "__main__":
    main()
