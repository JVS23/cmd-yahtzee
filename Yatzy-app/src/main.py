from dice import Dice
from scorelogic import Categories
from player import Player


def main():

    player = Player("Juho")
    player_score = Categories()
    dice_set = Dice()

    dice_set.roll()

    dice_set.choose()
    dice_set.choose()

    # fixthis
    test_set = dice_set.print()

    gained_score = player_score.check_chance(test_set)
    player.add_score(gained_score)
    #

    player.print_score()


main()
