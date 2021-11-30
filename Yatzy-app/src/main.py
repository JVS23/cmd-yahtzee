from dice import Dice
from scorelogic import Categories
from player import Player


def main():

    print("What's your name?")
    name_input = input()
    player = Player(name_input)
    player_score = Categories()
    dice_set = Dice()

    for i in range(15):

        print("\n ---Roll number", i + 1, "/ 15---\n")

        dice_set.roll()

        dice_set.choose()
        dice_set.choose()

        # replaced with pygame integration soon, useless to flesh out further currently

        print("What category do you want to choose?", 
             "(only works with Ones to Threes to not dilute the code needlessly)\n")
        method_list = [func for func in dir(player_score) if callable(
            getattr(player_score, func)) and not func.startswith("__")]

        print(method_list)

        user_input = str(input())

        if user_input == "check_aces":

            test_set = dice_set.print()

            gained_score = player_score.check_aces(test_set)
            player.add_score(gained_score)
            player.print_score()

        if user_input == "check_twos":

            test_set = dice_set.print()

            gained_score = player_score.check_twos(test_set)
            player.add_score(gained_score)
            player.print_score()

        if user_input == "check_threes":

            test_set = dice_set.print()

            gained_score = player_score.check_threes(test_set)
            player.add_score(gained_score)
            player.print_score()
            #

        dice_set.dicelist_reset()

    player.print_final_score()


main()
