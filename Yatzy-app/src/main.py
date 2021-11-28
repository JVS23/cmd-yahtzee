from dice import Dice
from scorelogic import Categories
from player import Player


def main():

    player = Player("Juho")
    player_score = Categories()
    dice_set1 = Dice()

    dice_set1.roll()

    dice_set1.choose()
    dice_set1.choose()

    # fixthis
    test_set = dice_set1.print()

    gained_score = player_score.three_of_a_kind(test_set)
    player.add_score(gained_score)
    #

    player.print_score()


main()
