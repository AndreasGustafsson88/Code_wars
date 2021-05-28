import random

ladders = [[2, 38], [7, 14], [8, 31], [15, 26], [21, 42], [36, 44], [28, 84], [51, 67], [71, 91], [78, 98], [87, 94]]
snakes = [[16, 6], [46, 25], [49, 11], [62, 19], [64, 60], [74, 53], [89, 68], [92, 88], [95, 75], [99, 80]]


class SnakesLadders:

    def __init__(self):
        self.p1 = 0
        self.p2 = 0
        self.p1_turn = True

    @staticmethod
    def move(player, d1, d2):
        player += d1 + d2
        return player

    @staticmethod
    def ladder(player):
        for i, rows in enumerate(ladders):
            if player in rows:
                return ladders[i][1]
        return player

    @staticmethod
    def snakes(player):
        for i, rows in enumerate(snakes):
            if player in rows:
                return snakes[i][1]
        return player

    @staticmethod
    def finish(player):
        return player == 100

    @staticmethod
    def over_100(player):
        return player > 100

    def play(self, die1, die2):
        if self.p1_turn:
            if self.finish(self.p2):
                return "Game over!"
            self.p1 = self.move(self.p1, die1, die2)


            if self.over_100(self.p1):
                self.p1 = 100 - (self.p1 - 100)

            if self.finish(self.p1):
                self.p1_turn = False
                return f"Player 1 Wins!"

            self.p1 = self.ladder(self.p1)
            self.p1 = self.snakes(self.p1)

            if self.p1 != 100:
                if die1 == die2:
                    self.p1_turn = True
                else:
                    self.p1_turn = False

            return f"Player 1 is on square {self.p1}"

        else:
            if self.finish(self.p1):
                return "Game over!"
            self.p2 = self.move(self.p2, die1, die2)

            if self.over_100(self.p2):
                self.p2 = 100 - (self.p2 - 100)

            if self.finish(self.p2):
                self.p1_turn = True
                return f"Player 2 Wins!"

            self.p2 = self.ladder(self.p2)
            self.p2 = self.snakes(self.p2)

            if self.p2 != 100:
                if die1 == die2:
                    self.p1_turn = False
                else:
                    self.p1_turn = True

            return f"Player 2 is on square {self.p2}"


def main():
    game = SnakesLadders()
    print(game.play(1, 1))

    print(game.play(1, 5))
    print(game.play(6, 2))
    print(game.play(1, 1))


if __name__ == "__main__":
    main()
