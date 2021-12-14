from tabulate import tabulate


class Player:
    """A class for creating player objects.

    Attributes:
        name: The name of the newly created player.
    """

    def __init__(self, name):
        """The class constructor, initialized the player object

        Args:
            name: The name of the newly created player.
        """

        self.name = name
        self.total_score = 0
        self.scoreboard = {"Aces": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0, "Bonus": 0,
                           "One pair": 0, "Two pairs": 0, "Three of a kind": 0, "Four of a kind": 0, "Yatzy": 0,
                           "Full house": 0, "Low straight": 0, "High straight": 0, "Chance": 0}

    def add_score(self, score, input):
        self.total_score += score
        print(self.name, "'s current total score is: ",
              self.total_score, "\n", sep="")
        print("\n")

        cap_input = str(input).capitalize()
        if cap_input in self.scoreboard.keys():
            self.scoreboard.update({cap_input: score})
        else:
            print("Error, category doesn't exist")

    def print_score(self):
        print(self.name, "'s current total score is: ",
              self.total_score, "\n", sep="")

    def print_scoreboard(self):
        hds = ["Categories", "Score"]
        print(tabulate(self.scoreboard.items(), headers=hds))

    def check_for_bonus(self):

        if int((self.scoreboard["Aces"])) + int((self.scoreboard["Twos"])) + int((self.scoreboard["Threes"])) + int((self.scoreboard["Fours"])) + \
                int((self.scoreboard["Fives"])) + int((self.scoreboard["Sixes"])) >= 63:
            print("You got the bonus! + 50 points\n")
            self.add_score(50, "Bonus")

    def print_final_score(self):
        print(self.name, "'s final score is:",
              self.total_score, ", good job!", sep="")
