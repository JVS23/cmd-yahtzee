import random as r


class Dice:
    def __init__(self):
        self.dice_list = []
        self.reroll_amount = 0

    def roll(self):

        for _ in range(5):
            self.dice_list.append(r.randint(1, 6))

        print("You rolled", self.dice_list, "\n")
        return self.dice_list

    def reroll(self, i):
        try:
            self.dice_list[i - 1] = r.randint(1, 6)
        except:
            print("An error occurred")

    def choose(self):
        state = True
        print(self.dice_list)
        choices = []
        indexes = [1, 2, 3, 4, 5]
        user_input = ""

        while state:
            print(
                "Choose the dice to reroll by index (+1), move to next roll with 7")
            while True:
                try:
                    user_input = int(input())
                except:
                    print("Invalid input, try again")
                    continue
                break

            if user_input not in indexes or user_input in choices:
                break
            choices.append(user_input)

        for i in choices:
            self.reroll(i)

        print("\nYour new dice: ", self.dice_list, "\n")
        return self.dice_list

    def dicelist_reset(self):
        self.dice_list = []

    def print(self):
        return self.dice_list
