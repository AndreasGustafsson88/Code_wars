import re

def song_decoder(song):
    return " ".join(re.sub("WUB", " ", song).split())


def main():
    print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))


if __name__ == "__main__":
    main()
