
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

        # To be refactored into own file

        print("Which category do you want to choose?\n")

        print("aces | twos | threes | fours | fives | sixes")
        print("one pair | two pairs | three of a kind | four of a kind | yatzy | chance")
        print("full house | low straight | high straight \n")

        inputmode = True

        while inputmode == True:
            user_input = str(input())

            current_dice = []

            if user_input == "aces":

                current_dice = dice_set.print()

                gained_score = player_score.check_aces(current_dice)
                player.add_score(gained_score, user_input)
                player.check_for_bonus()

            if user_input == "twos":

                current_dice = dice_set.print()

                gained_score = player_score.check_twos(current_dice)
                player.add_score(gained_score, user_input)
                player.check_for_bonus()

            if user_input == "threes":

                current_dice = dice_set.print()

                gained_score = player_score.check_threes(current_dice)
                player.add_score(gained_score, user_input)
                player.check_for_bonus()

            if user_input == "fours":

                current_dice = dice_set.print()

                gained_score = player_score.check_fours(current_dice)
                player.add_score(gained_score, user_input)
                player.check_for_bonus()

            if user_input == "fives":

                current_dice = dice_set.print()

                gained_score = player_score.check_fives(current_dice)
                player.add_score(gained_score, user_input)
                player.check_for_bonus()

            if user_input == "sixes":

                current_dice = dice_set.print()

                gained_score = player_score.check_sixes(current_dice)
                player.add_score(gained_score, user_input)
                player.check_for_bonus()

            if user_input == "one pair":

                current_dice = dice_set.print()

                gained_score = player_score.check_one_pair(current_dice)
                player.add_score(gained_score, user_input)

            if user_input == "two pairs":

                current_dice = dice_set.print()

                gained_score = player_score.check_two_pairs(current_dice)
                player.add_score(gained_score, user_input)

            if user_input == "three of a kind":

                current_dice = dice_set.print()

                gained_score = player_score.check_three_of_a_kind(current_dice)
                player.add_score(gained_score, user_input)

            if user_input == "four of a kind":

                current_dice = dice_set.print()

                gained_score = player_score.check_four_of_a_kind(current_dice)
                player.add_score(gained_score, user_input)

            if user_input == "yatzy":

                current_dice = dice_set.print()

                gained_score = player_score.check_yatzy(current_dice)
                player.add_score(gained_score, user_input)

            if user_input == "full house":

                current_dice = dice_set.print()

                gained_score = player_score.check_full_house(current_dice)
                player.add_score(gained_score, user_input)

            if user_input == "low straight":

                current_dice = dice_set.print()

                gained_score = player_score.check_low_straight(current_dice)
                player.add_score(gained_score, user_input)

            if user_input == "high straight":

                current_dice = dice_set.print()

                gained_score = player_score.check_high_straight(current_dice)
                player.add_score(gained_score, user_input)

            if user_input == "chance":

                current_dice = dice_set.print()

                gained_score = player_score.check_chance(current_dice)
                player.add_score(gained_score, user_input)

            if current_dice == []:
                print("Couldn't find the category, please type it again:")

            if current_dice != []:

                dice_set.dicelist_reset()
                player.print_scoreboard()
                player.print_score()
                inputmode = False

    player.print_final_score()


main()
