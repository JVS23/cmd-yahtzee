

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, score):
        self.score = self.score + score

    def print_score(self):
        print(self.name, "'s total score is: ", self.score)
