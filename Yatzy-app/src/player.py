

class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.scoreboard = {"Aces": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0,
                           "One pair": 0, "Two pairs": 0, "Three of a kind": 0, "Four of a kind": 0, "Yatzy": 0,
                           "Full house": 0, "Low straight": 0, "High straight": 0, "Chance": 0}

    def add_score(self, score):
        self.total_score += score
        print(self.name, "'s current total score is: ", self.total_score)

    def check_For_bonus(self):

        if self.total_score >= 63:
            self.total_score = self.total_score + 50

    def print_final_score(self):
        print(self.name, "'s final score is: ",
              self.total_score, ", good job!")
