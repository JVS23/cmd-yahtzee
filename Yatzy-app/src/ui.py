from dice import Dice
from scorelogic import Categories
from player import Player


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

        categories = Categories()
        dice_set = Dice()
        player_list = []
        turn_index = 0

        print("How many players do you want? (4 max)")
        self.init_players(player_list)
        player_amount = len(player_list)

        turn_amount = player_amount * 15

        for i in range(turn_amount):
            print("\n --- Roll number ", i + 1, " / ", turn_amount, ", ",
                  player_list[turn_index].name, "'s turn ---\n", sep="")

            dice_set.roll()
            dice_set.choose()
            print("\n")
            dice_set.choose()

            self.choose_category(player_list[turn_index], categories, dice_set)

            if turn_index + 1 == player_amount:
                turn_index = 0
            else:
                turn_index = turn_index + 1
        for i in range(player_amount):
            player_list[i].print_scoreboard()
            player_list[i].print_final_score()

    def init_players(self, player_list):
        """Creates a list for player objects.

        Args:
            player_list: List for the players.

        Raises:
            Exception: ValueError, if the user inputs a wrong kind of value.
        """

        while True:
            try:
                player_amount = int(input())
                if player_amount in (1, 2, 3, 4):
                    break
                else:
                    raise Exception("ValueError")
            except:
                print("Error, put in a valid number")

        for i in range(player_amount):
            player = self.create_player(i)
            player_list.append(player)

    def create_player(self, i):
        """Asks the user to name a player object, and creates one.

        Returns:
            Player object named as the user chose.
        """

        while True:

            print("Player ", i + 1, ", what's your name?", sep="")
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

        player.print_scoreboard()

        print("\nYour dice: ", dice_set.dice_return())

        print("\nWhich category do you want to choose?\n")

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
                    chosen_check = [1]
                    current_dice = []

            if user_input == "twos":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_twos(current_dice)
                if player.add_score(gained_score, user_input):
                    player.check_for_bonus()
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "threes":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_threes(current_dice)
                if player.add_score(gained_score, user_input):
                    player.check_for_bonus()
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "fours":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_fours(current_dice)
                if player.add_score(gained_score, user_input):
                    player.check_for_bonus()
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "fives":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_fives(current_dice)
                if player.add_score(gained_score, user_input):
                    player.check_for_bonus()
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "sixes":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_sixes(current_dice)
                if player.add_score(gained_score, user_input):
                    player.check_for_bonus()
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "one pair":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_one_pair(current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "two pairs":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_two_pairs(current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "three of a kind":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_three_of_a_kind(
                    current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "four of a kind":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_four_of_a_kind(
                    current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "yatzy":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_yatzy(current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "full house":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_full_house(current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "low straight":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_low_straight(
                    current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "high straight":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_high_straight(
                    current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [1]
                    current_dice = []

            if user_input == "chance":

                current_dice = dice_set.dice_return()

                gained_score = categories.check_chance(current_dice)
                if player.add_score(gained_score, user_input):
                    pass
                else:
                    chosen_check = [1]
                    current_dice = []

            if current_dice == [] and chosen_check == []:
                print("Couldn't find the category, please type it again:")

            if current_dice:

                dice_set.dice_list_reset()
                player.print_scoreboard()
                print("\n")
                player.print_score()
                inputmode = False
