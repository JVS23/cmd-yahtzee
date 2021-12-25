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
        self.scoreboard = {"Aces": 0,  "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0, "Bonus": 0,
                           "One pair": 0, "Two pairs": 0, "Three of a kind": 0, "Four of a kind": 0, "Yatzy": 0,
                           "Full house": 0, "Low straight": 0, "High straight": 0, "Chance": 0}
        self.scoreboardcheck = {"Aces": 0,  "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0, "Bonus": 0,
                                "One pair": 0, "Two pairs": 0, "Three of a kind": 0, "Four of a kind": 0, "Yatzy": 0,
                                "Full house": 0, "Low straight": 0, "High straight": 0, "Chance": 0}

    def add_score(self, score, input):
        """Adds score to the current players score total and scoreboard.

        Args:
            score: The amount of score added to the players score.
            input: The name of the category the player chose.

        Returns:
            Returns a boolean of True if the category is not chosen yet, False if it is.
        """

        cap_input = str(input).capitalize()

        if cap_input in self.scoreboard.keys():
            if int((self.scoreboardcheck[cap_input])) == 0:
                self.scoreboardcheck.update({cap_input: 1})
                self.scoreboard.update({cap_input: score})
                self.total_score += score

                print("Your score for", cap_input, "is:", score)
                print(self.name, "'s current total score is: ",
                      self.total_score, "\n", sep="")
                print("\n")
                return True
            else:
                print("Already chosen, choose another category")
                return False
        else:
            print("Error, category doesn't exist")
            return False

    def print_score(self):
        """Prints the players current score.
        """

        print(self.name, "'s current total score is: ",
              self.total_score, "\n", sep="")

    def print_scoreboard(self):
        """Prints the players whole scoreboard.
        """

        hds = ["Categories", "Score"]
        print(tabulate(self.scoreboard.items(), headers=hds))

    def check_for_bonus(self):
        """Checks if the player is eligible for the bonus points.
        """

        if int((self.scoreboard["Aces"])) + int((self.scoreboard["Twos"])) + int((self.scoreboard["Threes"])) + int((self.scoreboard["Fours"])) + \
                int((self.scoreboard["Fives"])) + int((self.scoreboard["Sixes"])) >= 63:
            print("You got the bonus! + 50 points\n")
            self.add_score(50, "Bonus")

    def print_final_score(self):
        """Prints the final score when the game ends.
        """

        print(self.name, "'s final score is:",
              self.total_score, ", good job!", sep="")
