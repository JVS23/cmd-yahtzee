import random as r


class Dice:
    def __init__(self):
        self.dice_list = []
        self.reroll_amount = 0

    def roll(self):

        for _ in range(5):
            self.dice_list.append(r.randint(1, 6))

        print("you rolled", self.dice_list)
        return self.dice_list

    def reroll(self, i):
        try:
            self.dice_list[i - 1] = r.randint(1, 6)
        except:
            print("An error occurred")

    def choose(self):
        state = True
        print("choose the dice to reroll")
        print(self.dice_list)
        choices = []
        indexes = [1, 2, 3, 4, 5]

        while state:
            print("choose the dice to reroll by index, move to next roll with 7")
            user_input = int(input())

            if user_input not in indexes or user_input in choices:
                break
            choices.append(user_input)

        for i in choices:
            self.reroll(i)

        print("Your new dice: ", self.dice_list)
        return self.dice_list
