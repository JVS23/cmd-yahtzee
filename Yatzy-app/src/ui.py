from dice import Dice
from scorelogic import Categories
from player import Player

# TODO  multiple players


class UI:
    """A class for generating the actual game loop.
    """

    def __init__(self):
        pass

    def start(self):
        self.run_ui()

    def run_ui(self):
        """Runs the game loop from start to finish.
        """

        player = self.create_player()
        categories = Categories()
        dice_set = Dice()

        for i in range(15):

            print("\n ---Roll number", i + 1, "/ 15---\n")

            dice_set.roll()
            dice_set.choose()
            dice_set.choose()

            self.choose_category(player, categories, dice_set)

        player.print_final_score()

    def create_player(self):
        """Asks the user to name a player object, and creates one.

        Returns:
            Player object named as the user chose.
        """

        while True:

            print("What's your name?")
            name_input = input()
            if len(name_input) > 0 and len(name_input) < 20:
                new_player = Player(name_input)
                return new_player

            print("ERROR: Pick a name with a character length of 1-20 characters\n")

    def choose_category(self, player, categories, dice_set):
        """Asks the user to choose the category, and allocates points to the chosen one.

        Args:
            player: the player in question.
            categories: all the different scoring categories.
            dice_set: the current rolled dice which this turn will be scored on.
        """

        print("Which category do you want to choose?\n")

        print("aces | twos | threes | fours | fives | sixes")
        print(
            "one pair | two pairs | three of a kind | four of a kind | yatzy | chance")
        print("full house | low straight | high straight \n")

        inputmode = True

        while inputmode is True:
            user_input = str(input())

            current_dice = []
            chosen_check = []

            if user_input == "aces":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_aces(current_dice)
                if player.add_score(gained_score, user_input):
                    player.check_for_bonus()
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "twos":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_twos(current_dice)
                if player.add_score(gained_score, user_input):
                    player.check_for_bonus()
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "threes":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_threes(current_dice)
                if player.add_score(gained_score, user_input):
                    player.check_for_bonus()
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "fours":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_fours(current_dice)
                if player.add_score(gained_score, user_input):
                    player.check_for_bonus()
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "fives":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_fives(current_dice)
                if player.add_score(gained_score, user_input):
                    player.check_for_bonus()
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "sixes":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_sixes(current_dice)
                if player.add_score(gained_score, user_input):
                    player.check_for_bonus()
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "one pair":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_one_pair(current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "two pairs":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_two_pairs(current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "three of a kind":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_three_of_a_kind(
                    current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "four of a kind":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_four_of_a_kind(
                    current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "yatzy":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_yatzy(current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "full house":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_full_house(current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "low straight":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_low_straight(
                    current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "high straight":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_high_straight(
                    current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [13]
                    current_dice = []

            if user_input == "chance":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_chance(current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [13]
                    current_dice = []

            if current_dice == [] and chosen_check == []:
                print("Couldn't find the category, please type it again:")

            if current_dice:

                dice_set.dice_list_reset()
                player.print_scoreboard()
                print("\n")
                player.print_score()
                inputmode = False
