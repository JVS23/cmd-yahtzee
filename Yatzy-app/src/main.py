
from dice import Dice
from scorelogic import Categories
from player import Player


# TODO: kbinput error, end, make scoreboard

def main():

    # print("What's your name?")
    name_input = "test"  # input()
    player = Player(name_input)
    player_score = Categories()
    dice_set = Dice()

    for i in range(15):

        print("\n ---Roll number", i + 1, "/ 15---\n")

        dice_set.roll()

        dice_set.choose()
        dice_set.choose()

        print("Which category do you want to choose?\n")

        print("aces | twos | threes | fours | fives | sixes")
        print("one pair | two pairs | three of a kind | four of a kind | yatzy | chance")
        print("full house | low straight | high straight")

        user_input = str(input())

        if user_input == "aces":

            current_dice = dice_set.print()

            gained_score = player_score.check_aces(current_dice)
            player.add_score(gained_score)

        if user_input == "twos":

            current_dice = dice_set.print()

            gained_score = player_score.check_twos(current_dice)
            player.add_score(gained_score)

        if user_input == "threes":

            current_dice = dice_set.print()

            gained_score = player_score.check_threes(current_dice)
            player.add_score(gained_score)

        dice_set.dicelist_reset()

    player.print_final_score()


main()
