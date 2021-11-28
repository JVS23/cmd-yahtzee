

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, score):
        self.score += score

    def check_For_bonus(self):

        if self.score >= 63:
            self.score = self.score + 50

    def print_score(self):
        print(self.name, "'s total score is: ", self.score)
