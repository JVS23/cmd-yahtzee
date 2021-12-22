import random as r


class Dice:
    """A class for creating the dice list and performing dice actions.
    """

    def __init__(self):
        self.dice_list = []

    def roll(self):
        """Fills an empty list with 5 dice.

        Returns:
            A list of five randomized dice.
        """

        for _ in range(5):
            self.dice_list.append(r.randint(1, 6))

        print("You rolled", self.dice_list, "\n")
        return self.dice_list

    def reroll(self, i):
        """Rerolls the chosen dice from the current list.

        Args:
            i: the indexes of the dice which will be rerolled.
        """

        try:
            self.dice_list[i - 1] = r.randint(1, 6)
        except:
            print("An error occurred")

    def choose(self):
        """The method where the user chooses which dice they want to reroll.

        Returns:
            The new dice list after the chosen dice have been rerolled.
        """

        state = True
        print(self.dice_list)
        choices = []
        indexes = [1, 2, 3, 4, 5]
        skip = [7]
        user_input = ""

        while state:
            print(
                "Choose the dice to reroll by index (+1), move to next roll with 7")
            while True:
                try:
                    user_input = int(input())
                    if user_input not in indexes and user_input not in skip:
                        raise Exception("InputError")
                except:
                    print("Invalid input, try again")
                    continue
                break

            if user_input in skip:
                break
            choices.append(user_input)

        for i in choices:
            self.reroll(i)

        print("\nYour new dice: ", self.dice_list, "\n")
        return self.dice_list

    def dice_list_reset(self):
        """Resets the current dice list.
        """

        self.dice_list = []

    def print(self):
        return self.dice_list
